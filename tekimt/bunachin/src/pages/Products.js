import React from 'react';
import ProductList from '../components/ProductList';

const products = [
  { id: 1, name: 'Ethiopian Coffee', description: 'Rich and full-bodied', price: 12 },
  { id: 2, name: 'Yemeni Coffee', description: 'Fruity and aromatic', price: 15 },
];

const Products = () => {
  return (
    <div>
      <ProductList products={products} />
    </div>
  );
};

export default Products;
