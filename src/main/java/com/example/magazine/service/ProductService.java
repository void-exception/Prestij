package com.example.magazine.service;

import com.example.magazine.model.Product;
import com.example.magazine.repository.ProductRepository;
import org.hibernate.jdbc.Expectation;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ProductService {

    private final ProductRepository productRepository;

    public ProductService(ProductRepository productRepository) {
        this.productRepository = productRepository;
    }


    public List<Product> getAllProducts(){
        return productRepository.findAll();
    }

    public Product getProduct(Long id){
        return productRepository.findById(id).orElse(null);
    }


    public List<Product> getProductsByCategoriy(String category){
        return productRepository.findAllByCategory(category);
    }

    public void createProduct(Product product){
        Product newProduct = new Product(product.getName(), product.getPrice(), product.getDescription(), product.getCategory(), product.getImg());
        productRepository.save(newProduct);
    }


}
