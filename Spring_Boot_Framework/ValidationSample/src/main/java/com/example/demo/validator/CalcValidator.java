package com.example.demo.validator;


import org.springframework.stereotype.Component;
import org.springframework.validation.Errors;
import org.springframework.validation.Validator;

import com.example.demo.form.CalcForm;

@Component
public class CalcValidator implements Validator {
    @Override
    public boolean supports(Class<?> clazz) {
        //인수로 전달받은 Form이 입력 체크의 대상인지를 논리값으로 돌려줌
        return CalcForm.class.isAssignableFrom(clazz);
    }

    @Override
    public void validate(Object target, Errors errors) {
        // 대상 Form 취득
        CalcForm form = (CalcForm) target;

        // 값이 입력되어 있는지 판단
        if (form.getLeftNum() != null && form.getRightNum() != null) {
            // 왼쪽 입력값이 홀수이고 오른쪽 입력값이 짝수가 아닌 경우
            if (!((form.getLeftNum() % 2 == 1) && (form.getLeftNum() % 2 == 0))) {
                // 에러인 경우 Errors 인터페이스의 reject 메서드
                // 에러 메세지의 키를 지정
                errors.reject("com.example.demo.validator.CalcValidator.message");
            }
        }
    }
}
