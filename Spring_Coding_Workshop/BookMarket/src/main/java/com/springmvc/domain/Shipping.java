package com.springmvc.domain;

import java.io.Serializable;
import java.util.Date;
import org.springframework.format.annotation.DateTimeFormat;

public class Shipping implements Serializable {
	
	private static final long serialVersionUID = 8121814661110003493l;
	
	// 硅价 绊按 捞抚
	private String name;
	
	// 硅价老
	@DateTimeFormat(pattern = "yyyy/MM/dd")
	private Date date;
	
	// 硅价 林家 按眉
	private Address address;

	public Shipping() {
		this.address = new Address();
		// TODO Auto-generated constructor stub
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public Date getDate() {
		return date;
	}

	public void setDate(Date date) {
		this.date = date;
	}

	public Address getAddress() {
		return address;
	}

	public void setAddress(Address address) {
		this.address = address;
	}


}
