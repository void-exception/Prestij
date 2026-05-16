package com.example.magazine.controller;

import com.example.magazine.service.ProductService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/page")
public class PageController {

    private final ProductService productService;

    public PageController(ProductService productService) {
        this.productService = productService;
    }




    @GetMapping("/products")
    public String allProducts(Model model){
        model.addAttribute("products", productService.getAllProducts());
        model.addAttribute("categories", productService.allCat());
        return "products";
    }

    @GetMapping("/products/{cat}")
    public String catProducts(Model model, @PathVariable String cat){
        model.addAttribute("products", productService.getProductsByCategoriy(cat));
        model.addAttribute("categories", productService.allCat());
        return "products";
    }
}
