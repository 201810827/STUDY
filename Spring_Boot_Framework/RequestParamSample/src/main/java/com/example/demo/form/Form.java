package com.example.demo.form;

import java.time.LocalDate;
import org.springframework.format.annotation.DateTimeFormat;
import lombok.Data;

//데이터 받아옴
@Data
public class Form {
    private String name;
    private Integer age;

    @DateTimeFormat(iso = DateTimeFormat.ISO.DATE)
    private LocalDate birth;
}
