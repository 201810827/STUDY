package com.springmvc.exception;

@SuppressWarnings("serial")
public class BookIdException extends RuntimeException {
	
	private String bookId;
	
	// »ý¼ºÀÚ
	public BookIdException(String bookId) {
		this.bookId = bookId;
	}
	
	// Getter()
	public String getBookId() {
		return bookId;
	}

}
