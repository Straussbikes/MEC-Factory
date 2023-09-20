<template>
  <div class="responsive-page">
    <div class="login-container">
      <h1 class="login-titles">Registration Form</h1>
      <form @submit.prevent="register" class="login-form">
        <div class="form-group">
          <label for="name" class="form-label">Name:</label>
          <input type="text" id="name" v-model="name" class="form-input" required />
        </div>
        <div class="form-group">
          <label for="email" class="form-label">Email:</label>
          <input type="email" id="email" v-model="email" class="form-input" required />
        </div>
        <div class="form-group">
          <label for="password" class="form-label">Password:</label>
          <input type="password" id="password" v-model="password" class="form-input" required />
        </div>
        <div class="form-group">
          <label for="passwordConfirmation" class="form-label">Confirm Password:</label>
          <input
            type="password"
            id="passwordConfirmation"
            v-model="passwordConfirmation"
            class="form-input"
            required
          />
        </div>
        <button type="submit" class="login-button">Register</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  // ... (other component code)

  methods: {
    async register() {
      if (this.password !== this.passwordConfirmation) {
        alert('Password and password confirmation do not match.');
        return;
      }

      try {
        const response = await axios.post('http://localhost:5000/api/v1/register', {
          "name": this.name,
           "email": this.email,
          "password": this.password,
          "repassword":this.passwordConfirmation
        });
        
        console.log('Registration successful:', response.data);
        await this.$router.push({path:"/login"});
      } catch (error) {
        console.error('Registration failed:', error);
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
    justify-content: center;
    align-items: center;
    height: 84.5vh; /* Adjust height to cover the full viewport */
    background-color: rgb(4, 26, 59);
  }
  

  
  .login-titles {
    color: white;
    display: flex;
    margin-bottom: 20px ;
    margin-left: 10px;
    
    
  }
  
  .login-form {
    display: flex;
    flex-direction: column;
  }
  
  .form-group {
    margin-bottom: 16px;
  }
  
  .form-label {
    color: white;
    
  }
  
  .form-input {
    width: 100%;
    padding: 5px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .login-button {
    background-color: #007bff;
    color: white;
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
  