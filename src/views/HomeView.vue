<template>
  <div class="page">
    <h1 class="title">Welcome</h1>
    <div class="baixo">
    <v-row class="button-container">
      <button class="btn" @click="handleClick">
        <i class="fa fa-star"></i> Login
      </button>
      <button class="btn" @click="goToNewPage">
        <i class="fa fa-star"></i> Register
      </button>
    </v-row>
  </div>
  </div>
</template>

<script>
export default { 
  name: 'HomeView',
  methods: {
    goToNewPage() {
      this.$router.push("/register");
    },
    handleClick(){
      this.$router.push("/login");
    }
  },
  
}
</script>

<style >

.page{
  height: 84.5vh;
}
.title {
  font-size: 32px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  margin-top: 200px;
  margin-right: 15px;
  
}
.baixo{
  display: flex;
  margin-top: 200px;
}

.button-container {
  display:flex;
  justify-content:center;
  align-items: center;
 
 
    /* Media query for smaller screens (max-width: 768px) */
    @media (max-width: 768px) {
      flex-direction: column; /* Display vertically */
      
    }
}

.btn {
  background-color: #007bff;
  color: white;
  padding: 15px 30px;
  border: none;
  border-radius: 4px;
  width: 150px;
  cursor: pointer;
  margin: 0 50px; /* Add space between buttons */
  transition: background-color 0.3s ease;
  @media (max-width: 768px) {
    margin: 10px 0; /* Vertical distance of 20px */
  }
}

.btn:hover {
  background-color: #003f7f;
}
</style>