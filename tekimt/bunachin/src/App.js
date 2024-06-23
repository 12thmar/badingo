import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import Home from './pages/Home';
import Products from './pages/Products';
import About from './components/About';
import Contact from './components/Contact';
import ProductDetail from './components/ProductDetail';

const App = () => {
  const products = [
    { id: 1, name: 'Ethiopian Coffee', description: 'Rich and full-bodied', price: 12 },
    { id: 2, name: 'Yemeni Coffee', description: 'Fruity and aromatic', price: 15 },
  ];

  return (
    <Router>
      <Header />
      <main>
        <Routes>
          <Route exact path="/" component={Home} />
          <Route exact path="/products" component={Products} />
          <Route path="/products/:productId" render={() => <ProductDetail products={products} />} />
          <Route path="/about" component={About} />
          <Route path="/contact" component={Contact} />
        </Routes>
      </main>
      <Footer />
    </Router>
  );
};

export default App;
