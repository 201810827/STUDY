package com.springmvc.domain;

import java.io.Serializable;

public class Order implements Serializable {
	
	private static final long serialVersionUID = 2659461092439119863L;
	
	// �ֹ� ID
	private Long orderId;
	
	// ��ٱ��� ��ü
	private Cart cart;
	
	// ���� ��ü
	private Customer customer;
	
	// ����� ��ü
	private Shipping shipping;

	public Order() {
		this.customer = new Customer();
		this.shipping = new Shipping();
		// TODO Auto-generated constructor stub
	}

	public Long getOrderId() {
		return orderId;
	}

	public void setOrderId(Long orderId) {
		this.orderId = orderId;
	}

	public Cart getCart() {
		return cart;
	}

	public void setCart(Cart cart) {
		this.cart = cart;
	}

	public Customer getCustomer() {
		return customer;
	}

	public void setCustomer(Customer customer) {
		this.customer = customer;
	}

	public Shipping getShipping() {
		return shipping;
	}

	public void setShipping(Shipping shipping) {
		this.shipping = shipping;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((orderId == null) ? 0 : orderId.hashCode());
		
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Order other = (Order) obj;
		if (orderId == null) {
			if (other.orderId != null)
				return false;
		} else if (!orderId.equals(other.orderId))
			return false;
		
		return true;
	}
	
	
}
