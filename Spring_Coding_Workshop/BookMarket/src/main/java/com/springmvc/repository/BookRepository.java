package com.springmvc.repository;

import java.util.List;
import java.util.Map;
import java.util.Set;
import com.springmvc.domain.Book;

public interface BookRepository {
	
	// 모든 도서 열람
	List<Book> getAllBookList();
	// 카테고리 별 도서 열람
	List<Book> getBookListByCategory(String category);
	// 출판사와 카테고리 값으로 필터링한 도서 열람
	Set<Book> getBookListByFilter(Map<String, List<String>> filter);
	// 도서 ID와 일치하는 도서 열람
	Book getBookById(String bookId);
	// 신규 도서 등록
	void setNewBook(Book book);
	// 도서 정보 수정
	void setUpdateBook(Book book);
	// 도서 삭제
	void setDeleteBook(String bookID);
	
}
