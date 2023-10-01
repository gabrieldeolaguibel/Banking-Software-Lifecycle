<template>
    <div class="home-container">
      <h1>Welcome to IE Bank</h1>
      <p>Your trusted partner for all banking needs.</p>
      <div class="navigation-buttons">
        <router-link to="/skull" class="nav-button">Skull</router-link>
        <router-link to="/accounts" class="nav-button">Accounts</router-link>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "Home"
  };
  </script>
  
  <style scoped>
  .home-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 80vh;
  }
  
  h1 {
    font-size: 2.5em;
    margin-bottom: 20px;
  }
  
  .navigation-buttons {
    display: flex;
    gap: 20px;
  }
  
  .nav-button {
    padding: 10px 20px;
    background-color: #3498db;
    color: white;
    border: none;
    border-radius: 5px;
    text-decoration: none;
    transition: background-color 0.3s;
  }
  
  .nav-button:hover {
    background-color: #2980b9;
  }
  </style>
  