package com.springmvc.validator;

import org.springframework.stereotype.Component;
import org.springframework.validation.Validator;
import org.springframework.validation.Errors;
import com.springmvc.domain.Book;

@Component
public class UnitsInStockValidator implements Validator {
	
	public boolean supports(Class<?> clazz) {
		// Book Ŭ������ ��ȿ�� �˻� ���θ� ���� �޼ҵ�
		
		return Book.class.isAssignableFrom(clazz);
	}
	
	public void validate(Object target, Errors errors) {
		// Book Ŭ������ ��ȿ�� �˻� �޼ҵ�
		
		Book book = (Book) target;
		
		if (book.getUnitPrice() >= 10000 && book.getUnitsInStock() > 99) {
			// ���� ��ü�� �Ӽ��� �޽��� ����
			
			errors.rejectValue("unitsInStock", "UnitsInStockValidator.message");
		}
	}

}
