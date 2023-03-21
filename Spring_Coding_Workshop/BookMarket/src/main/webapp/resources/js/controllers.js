function addToCart(action) {
	document.addForm.action = action;
	document.addForm.submit();
	
	alert("도서가 장바구니에 추가되었습니다.");
}

function removeFromCart(action) {
	document.removeForm.action = action;
	document.removeForm.submit();
	
	alert("도서가 장바구니에서 삭제되었습니다. 새로고침을 실행해주세요.");

}

function clearCart() {
	document.clearForm.submit();
	
	alert("모든 도서가 장바구니에서 삭제되었습니다. 새로고침을 실행해주세요.");
}

function deleteConfirm(id) {
	if (confirm("삭제합니다!!") == true) location.href = "./delete?id=" + id;
	else return;
}