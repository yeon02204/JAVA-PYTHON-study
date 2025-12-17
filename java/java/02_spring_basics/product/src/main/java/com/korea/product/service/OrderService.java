package com.korea.product.service;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.korea.product.dto.OrderDTO;
import com.korea.product.model.OrderEntity;
import com.korea.product.model.ProductEntity;
import com.korea.product.persistence.OrderRepository;
import com.korea.product.persistence.ProductRepository;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class OrderService {
	
	private final OrderRepository orderRepository;
	private final ProductRepository productRepository;
	// 주문내역 조회하기
	public List<OrderDTO> getAllOrderTotalPrices(){
		// select한 결과를 List에 담는다
		List<Object[]> results = orderRepository.findAllOrderTotalPrices();
		
		return OrderDTO.toListOrderDTO(results);
	}
	public List<OrderDTO> save(OrderDTO dto) {
		Optional<ProductEntity> option = productRepository.findById(dto.getProductId());
		ProductEntity productEntity;
		
		if(option.isPresent()) {
			productEntity = option.get();
		}else {
			throw new IllegalArgumentException("상품을 찾을 수 없다");
		}
		
		// 재고가 있는지 확인
		if(productEntity.getProductStock() < dto.getProductCount()) {
			throw new RuntimeException("재고가 부족합니다 , 현재 제고 : " + productEntity.getProductStock());
		}
		
		// 주문하기
		OrderEntity order =OrderEntity.builder()
				.product(productEntity)
				.productCount(dto.getProductCount())
				.build();
		
		orderRepository.save(order);
		
		// 재고 감소(productEntity의 재고 - 주문한 갯수)
		// 디비에 수정된 재고로 다시 업데이트
		  //전체 상품 목록을 조회해서 반환
		return null;
	}
	
}
