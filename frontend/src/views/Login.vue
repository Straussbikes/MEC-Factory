<template>
  <div class="responsive-page">
   
    
    <div class="login-form-container">
    <form @submit.prevent="submitForm" class="login-form">
      <h1 class="login-title">Login</h1>
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required />
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit" class="login-button">Login</button>
    </form>
    </div>
  </div>
  
  </template>
  
  <script>

import axios from 'axios';
import { nextTick } from 'vue';
import {ref} from "vue";
import { useUserStore } from '@/services/user-store';

 // Import your user store
const userStore = useUserStore();

  export default {
    data() {
      return {
        email: '',
        password: '',
      };
    },
    methods: {
        async submitForm() {
        try {
        const response = await axios.post('/login', {
           "email": this.email,
          "password": this.password,
        });
        userStore.token=response.data.ok;
        userStore.expiresIn=response.data.expiresIn;
        userStore.setTime();      
        if(response.status==200) {
          userStore.isLoggedIn=true;
          localStorage.setItem('isLoggedIn', true);
          try {
              const res = await axios({
                method: 'GET',
                url:'/protected',
                headers:{
                  'Authorization':"Bearer " + userStore.token
                },
              })
              userStore.name=res.data.name;
              localStorage.setItem('name', res.data.name);
              localStorage.setItem('emaila',this.email);
          } catch (error) {
            console.log(error)
          }
          
          await this.$router.push({path:"/main"});
          location.reload();
        }
        console.log('Login successful:', response.data);
      } catch (error) {
        console.error('Login failed:', error);
      }
      },
    },
  };

  </script>
  
  <style>
  body {
    margin: 0;
    padding: 0;
    
  }
  
  .responsive-page {
    display: flex;
    flex-direction: column; /* Set the direction to column */
    justify-content: center; /* Center vertically */
    align-items: center; /* Center horizontally */
    height: 84.5vh;
    background-color: rgb(4, 26, 59);
  }
  
  .login-form-container {
    margin-top: 20px; /* Add some space between the title and form */
    
  }
  
  .login-form {
    background-color: rgb(61, 131, 236);
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    padding: 40px;
    max-width: 400px;
    width: 100%;
    justify-content:center;
    align-items: center;
    
  }
  
  .form-group {
    margin-bottom: 16px;
  }
  
  label {
    display: block;
    margin-bottom: 8px;
  }
  .login-title {
    color: white;
    font-size: 34px; /* Adjust the font size as needed */
    margin-bottom: 30px; /* Add space below the title */
    margin-left: 0px;
    text-align: center;
   
  }
  
  input {
  
      width: 100%;
      padding: 5px;
      border: 1px solid #ccc;
      border-radius: 4px;
      background-color: #fff; 
    
  }
  
  .login-button {
    background-color: #007bff;
    color: #ffffff;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .login-button:hover {
    background-color: #0056b3;
  }
  </style>
  