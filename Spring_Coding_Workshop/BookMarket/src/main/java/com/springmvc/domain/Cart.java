package com.springmvc.domain;

import java.util.HashMap;
import java.util.Map;
import java.io.Serializable;

public class Cart implements Serializable {
	
	private static final long serialVersionUID = 2155125089108199199L;
	
	private String cartId;
	private Map<String, CartItem> cartItems;
	private int grandTotal;
	
	public Cart() {
		cartItems = new HashMap<String, CartItem>();
		grandTotal = 0;
		// TODO Auto-generated constructor stub
	}

	public Cart(String cartId) {
		this();
		this.cartId = cartId;
	}

	public String getCartId() {
		return cartId;
	}

	public void setCartId(String cartId) {
		this.cartId = cartId;
	}

	public Map<String, CartItem> getCartItems() {
		return cartItems;
	}

	public void setCartItems(Map<String, CartItem> cartItems) {
		this.cartItems = cartItems;
	}

	public int getGrandTotal() {
		return grandTotal;
	}

	public void updateGrandTotal() {
		grandTotal = 0;
		for (CartItem item : cartItems.values()) {
			grandTotal = grandTotal + item.getTotalPrice();
		}
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((cartId == null) ? 0 : cartId.hashCode());
		
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
		Cart other = (Cart) obj;
		if (cartId == null) {
			if (other.cartId != null)
				return false;
		} else if (!cartId.equals(other.cartId))
			return false;
		
		return true;
	}
	
	public void addCartItem(CartItem item) {
		
		// 현재 등록하기 위한 도서 ID 가져오기
		String bookId = item.getBook().getBookId();
		
		// 도서 ID가 cartItems 객체에 등록되어 있는지 여부 확인
		if (cartItems.containsKey(bookId)) {
			
			// 등록된 도서 ID에 대한 정보 가져오기
			CartItem cartItem = cartItems.get(bookId);
			//등록된 도서 ID의 개수 추가 저장
			cartItem.setQuantity(cartItem.getQuantity() + item.getQuantity());
			// 등록된 도서 ID에 대한 변경 정보 저장
			cartItems.put(bookId, cartItem);
		} else {
			// 도서 ID에 대한 도서 정보 저장
			cartItems.put(bookId, item);
		}
		
		// 총액 갱신
		updateGrandTotal();
	}
	
	
	// 도서 삭제
	public void removeCartItem(CartItem item) {
		String bookId = item.getBook().getBookId();
		// 도서 삭제
		cartItems.remove(bookId);
		
		//총액 갱신
		updateGrandTotal();
	}
	
}
