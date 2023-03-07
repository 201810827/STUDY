package com.example.quiz.service;

import java.util.Optional;
import com.example.quiz.entity.Quiz;
import org.springframework.data.jdbc.repository.query.Query;

public interface QuizService {

    // 등록된 모든 퀴즈 가져오기
    Iterable<Quiz> selectAll();

    // id를 이용하여 한 건 가져오기
    Optional<Quiz> selectOneById(Integer Id);

    // 랜덤 취득
    Optional<Quiz> selectOneRandomQuiz();

    // 정답 / 오답 판단
    Boolean checkQuiz(Integer id, Boolean myAnswer);

    // 퀴즈 등록
    void insertQuiz(Quiz quiz);

    // 퀴즈 변경
    void updateQuiz(Quiz quiz);

    // 퀴즈 삭제
    void deleteQuizById(Integer Id);

}
