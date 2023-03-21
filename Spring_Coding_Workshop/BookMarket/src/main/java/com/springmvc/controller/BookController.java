package com.springmvc.controller;

import java.util.List;
import java.util.Map;
import java.util.Set;
import java.io.File;

import org.springframework.web.bind.annotation.MatrixVariable;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
//import org.springframework.web.bind.annotation.RequestMethod;

import com.springmvc.domain.Book;
import com.springmvc.service.BookService;
import com.springmvc.exception.CategoryException;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.servlet.ModelAndView;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.WebDataBinder;
import org.springframework.web.bind.annotation.InitBinder;
import org.springframework.web.multipart.MultipartFile;

import javax.servlet.http.HttpServletRequest;
import org.springframework.web.bind.annotation.ExceptionHandler;
import com.springmvc.exception.BookIdException;


import javax.validation.Valid;
import org.springframework.validation.BindingResult;
import com.springmvc.validator.UnitsInStockValidator;
import com.springmvc.validator.BookValidator;

@Controller
@RequestMapping("/books")
public class BookController {
	
	@Autowired
	private BookService bookService;
	
	@Autowired
	private BookValidator bookValidator;
	//private UnitsInStockValidator unitsInStockValidator;
	
	@GetMapping
	//@RequestMapping
	//(value = "/books", method = RequestMethod.GET)
	public String requstBookList(Model model) {
		
		List<Book> list = bookService.getAllBookList();
		model.addAttribute("bookList", list);
		
		return "books";
	}
	
	@GetMapping("/all")
	//@RequestMapping("/all")
	public ModelAndView requestAllBooks() {
		
		ModelAndView modelAndView = new ModelAndView();
		
		List<Book> list = bookService.getAllBookList();
		modelAndView.addObject("bookList", list);
		modelAndView.setViewName("books");
		
		return modelAndView;
	}
	
	@GetMapping("/{category}")
	public String requestBooksByCategory(@PathVariable("category") String bookCategory, Model model) {
		
		List<Book> booksByCategory = bookService.getBookListByCategory(bookCategory);
		
		if (booksByCategory == null || booksByCategory.isEmpty()) {
			throw new CategoryException();
		}
		
		model.addAttribute("bookList", booksByCategory);
		
		return "books";
	}
	
	@GetMapping("/filter/{bookFilter}")
	public String requestBooksByFilter(@MatrixVariable(pathVar = "bookFilter") Map<String, List<String>> bookFilter, Model model) {
		
		Set<Book> booksByFilter = bookService.getBookListByFilter(bookFilter);
		model.addAttribute("bookList", booksByFilter);
		
		return "books";
	}
	
	@GetMapping("/book")
	public String requestBookById(@RequestParam("id") String bookId, Model model) {
		Book bookById = bookService.getBookById(bookId);
		model.addAttribute("book", bookById);
		
		return "book";
	}
	
	// 신규 도서 등록
	@GetMapping("/add")
	public String requestAddBookForm(@ModelAttribute("NewBook") Book book) {
		return "addBook";
	}
	
	@PostMapping("/add")
	public String submitAddNewBook(@Valid @ModelAttribute("NewBook") Book book,
									BindingResult result) {
		
		if (result.hasErrors()) {
			return "addBook";
		}
		
		MultipartFile bookImage = book.getBookImage();
		
		String saveName = bookImage.getOriginalFilename();
		File saveFile = new File("C:\\upload", saveName);
		
		if (bookImage != null && !bookImage.isEmpty()) {
			try {
				bookImage.transferTo(saveFile);
				book.setFileName(saveName);
			} catch (Exception e) {
				throw new RuntimeException("도서 이미지 업로드에 실패하였습니다.", e);
			}
		}
		
		bookService.setNewBook(book);
		
		return "redirect:/books";
	}
	
	@ModelAttribute
	public void addAttributes(Model model) {
		model.addAttribute("addTitle", "신규 도서 등록");
	}
	
	@InitBinder
	public void initBinder(WebDataBinder binder) {
		//binder.setValidator(unitsInStockValidator);
		binder.setValidator(bookValidator);
		binder.setAllowedFields("bookId", "name", "unitPrice", "author", "description",
				"publisher", "category", "unitsInStock", "totalPages", "releaseDate", "condition", "bookImage");
	}
	
	@ExceptionHandler(value = {BookIdException.class})
	public ModelAndView handelrError(HttpServletRequest req, BookIdException exception) {
		ModelAndView mav = new ModelAndView();
		
		// 요청한 도서 ID 저장
		mav.addObject("invalidBookId", exception.getBookId());
		// 예외 처리 클래스 저장
		mav.addObject("exception", exception);
		// 요청 URL과 요청 쿼리문 저장
		mav.addObject("url", req.getRequestURL() + "?" + req.getQueryString());
		// errorBook 뷰에서 파일 출력
		mav.setViewName("errorBook");
		
		return mav;
	}
	
	// 도서 정보 수정(GET)
	@GetMapping("/update")
	public String getUpdateBookForm(@ModelAttribute("updateBook") Book book,
			@RequestParam("id") String bookId, Model model) {
		
		Book bookById = bookService.getBookById(bookId);
		model.addAttribute("book", bookById);
		
		return "updateForm";
	
	}
	
	@PostMapping("/update")
	public String submitUpdateBookForm(@ModelAttribute("updateBook") Book book) {
		
		MultipartFile bookImage = book.getBookImage();
		String rootDirectory = "c:/upload/";
		
		if (bookImage != null && !bookImage.isEmpty()) {
			try {
				String fname = bookImage.getOriginalFilename();
				bookImage.transferTo(new File("c:/upload/" + fname));
				
				book.setFileName(fname);
			} catch(Exception e) {
				throw new RuntimeException("Book Image saved failed", e);
			}
		}
		
		bookService.setUpdateBook(book);
		
		return "redirect:/books";
	}
	
	@RequestMapping(value = "/delete")
	public String getDeleteBookForm(Model model, @RequestParam("id") String bookId) {
		
		bookService.setDeleteBook(bookId);
		
		return "redirect:/books";
		
	}
	
}
