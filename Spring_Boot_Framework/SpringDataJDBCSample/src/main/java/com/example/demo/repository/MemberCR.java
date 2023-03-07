package com.example.demo.repository;

import org.springframework.data.repository.CrudRepository;
import com.example.demo.entity.Member;

public interface MemberCR extends CrudRepository<Member, Integer>{

}
