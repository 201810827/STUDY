package com.example.quiz.controller;

import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import com.example.quiz.entity.Quiz;
import com.example.quiz.form.QuizForm;
import com.example.quiz.service.QuizService;

@Controller
@RequestMapping("/quiz")
public class QuizController {

    @Autowired
    QuizService service;

    @ModelAttribute
    public QuizForm setUpForm() {
        QuizForm form = new QuizForm();
        form.setAnswer(true);

        return form;
    }

    @GetMapping
    public String showList(QuizForm quizForm, Model model) {
        quizForm.setNewQuiz(true);
        Iterable<Quiz> list = service.selectAll();

        model.addAttribute("list", list);
        model.addAttribute("title", "등록 폼");

        return "crud";
    }

    @PostMapping("/insert")
    public String insert(@Validated QuizForm quizForm, BindingResult bindingResult,
                         Model model, RedirectAttributes redirectAttributes) {

        // Form에서 Entity로 넣기
        Quiz quiz = new Quiz();
        quiz.setQuestion(quizForm.getQuestion());
        quiz.setAnswer(quizForm.getAnswer());
        quiz.setAuthor(quizForm.getAuthor());

        // 입력 체크
        if (!bindingResult.hasErrors()) {
            service.insertQuiz(quiz);
            redirectAttributes.addFlashAttribute("complete", "등록이 완료되었습니다");

            return "redirect:/quiz";
        } else {
            // 에러 발생 시, 목록 표시
            return showList(quizForm, model);
        }
    }

    @GetMapping("/{id}")
    public String showUpdate(QuizForm quizForm, @PathVariable Integer id, Model model) {
        // Quiz 취득
        Optional<Quiz> quizOpt = service.selectOneById(id);

        // QuizForm에 채워넣기
        Optional<QuizForm> quizFormOpt = quizOpt.map(t -> makeQuizForm(t));

        // QuizForm이 null이 아니라면 취득
        if(quizFormOpt.isPresent()) {
            quizForm = quizFormOpt.get();
        }

        // 변경용 모델
        makeUpdateModel(quizForm, model);
        return "crud";
    }

    // 변경용 모델 생성
    private void makeUpdateModel(QuizForm quizForm, Model model) {
        model.addAttribute("id", quizForm.getId());
        quizForm.setNewQuiz(false);
        model.addAttribute("quizForm", quizForm);
        model.addAttribute("title", "변경 폼");
    }

    // id를 키로 사용
    @PostMapping("/update")
    public String update(@Validated QuizForm quizForm, BindingResult result,
                         Model model, RedirectAttributes redirectAttributes) {
        // Quiz Form에서 quiz로 채우기
        Quiz quiz = makeQuiz(quizForm);

        if (!result.hasErrors()) {
            // 변경 처리
            service.updateQuiz(quiz);
            // 리다이렉트
            redirectAttributes.addFlashAttribute("complete", "변경이 완료되었습니다.");
            return "redirct:/quiz/" + quiz.getId();
        } else {
            // 변경용 모델 생성
            makeUpdateModel(quizForm, model);
            return("crud");
        }
    }

    private Quiz makeQuiz(QuizForm quizForm) {
        Quiz quiz = new Quiz();
        quiz.setId(quizForm.getId());
        quiz.setQuestion(quizForm.getQuestion());
        quiz.setAnswer(quizForm.getAnswer());
        quiz.setAuthor(quizForm.getAuthor());

        return quiz;
    }

    private QuizForm makeQuizForm(Quiz quiz) {
        QuizForm form = new QuizForm();
        form.setId(quiz.getId());
        form.setQuestion(quiz.getQuestion());
        form.setAnswer(quiz.getAnswer());
        form.setAuthor(quiz.getAuthor());
        form.setNewQuiz(false);

        return form;
    }

    @PostMapping("/delete")
    public String delete (@RequestParam("id") String id,
                          Model model, RedirectAttributes redirectAttributes) {
        // 퀴즈 정보 1건 삭제 후 리다이렉트
        service.deleteQuizById(Integer.parseInt(id));
        redirectAttributes.addFlashAttribute("delcomplete", "삭제 완료했습니다.");
        return "redirect:/quiz";
    }

    @GetMapping("/play")
    public String showQuiz(QuizForm quizForm, Model model) {
        // Quiz 정보 취득
        Optional<Quiz> quizOpt = service.selectOneRandomQuiz();

        // 값이 있는지 확인
        if (quizOpt.isPresent()) {
            Optional<QuizForm> quizFormOpt = quizOpt.map(t -> makeQuizForm(t));
            quizForm = quizFormOpt.get();
        } else {
            model.addAttribute("msg", "등록된 문제가 없습니다.");
            return "play";
        }

        // 표시용 모델에 저장
        model.addAttribute("quizForm", quizForm);
        return "play";
    }

    // 퀴즈 채점
    @PostMapping("/check")
    public String checkQuiz(QuizForm quizForm, @RequestParam Boolean answer, Model model) {
        if (service.checkQuiz(quizForm.getId(), answer)) {
            model.addAttribute("msg", "정답입니다.");
        } else {
            model.addAttribute("msg", "오답입니다.");
        }
        return "answer";
    }
}
