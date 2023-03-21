package com.springmvc.repository;

import java.util.List;
import java.util.Map;
import java.util.Set;
import com.springmvc.domain.Book;

public interface BookRepository {
	
	// ��� ���� ����
	List<Book> getAllBookList();
	// ī�װ� �� ���� ����
	List<Book> getBookListByCategory(String category);
	// ���ǻ�� ī�װ� ������ ���͸��� ���� ����
	Set<Book> getBookListByFilter(Map<String, List<String>> filter);
	// ���� ID�� ��ġ�ϴ� ���� ����
	Book getBookById(String bookId);
	// �ű� ���� ���
	void setNewBook(Book book);
	// ���� ���� ����
	void setUpdateBook(Book book);
	// ���� ����
	void setDeleteBook(String bookID);
	
}
