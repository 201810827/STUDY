package com.springmvc.repository;

import java.util.HashMap;
import java.util.Map;
import org.springframework.stereotype.Repository;
import com.springmvc.domain.Cart;

@Repository
public class CartRepositoryImpl implements CartRepository {
	
	
	private Map<String, Cart> listOfCarts;
	
	public CartRepositoryImpl() {
		listOfCarts = new HashMap<String, Cart>();
	}
	
	// 새로운 장바구니 생성, 장바구니 ID 등록하고 생성된 장바구니 객체 반환
	public Cart create(Cart cart) {
		if (listOfCarts.keySet().contains(cart.getCartId())) {
			throw new IllegalArgumentException(String.format("장바구니를 생성할 수 없습니다. 장바구니 id(%)가 존재합니다", cart.getCartId()));
		}
		
		listOfCarts.put(cart.getCartId(), cart);
		return cart;
	}
	
	// 장바구니 ID를 이용하여 장바구니의 모든 정보 반환
	public Cart read(String cartId) {
		return listOfCarts.get(cartId);
	}
	
	public void update(String cartId, Cart cart) {
		
		if (!listOfCarts.keySet().contains(cartId)) {
			
			// 장바구니 ID가 존재하지 않은 경우 예외 처리
			throw new IllegalArgumentException(String.format("장바구니 목록을 갱신할 수 없습니다. 장바구니 id(%)가 존재하지 않습니다.", cartId));
		
		} 
		
		listOfCarts.put(cartId, cart);
		
	}
	
	public void delete(String cartId) {
		
		if (!listOfCarts.keySet().contains(cartId)) {
			
			// 장바구니 ID가 존재하지 않으면 예외
			throw new IllegalArgumentException(String.format("장바구니 목록을 삭제할 수 없습니다. 장바구니 id(%)가 존재하지 않습니다.", cartId));
		
		}
		
		listOfCarts.remove(cartId);
		
	}


}
