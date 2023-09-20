<template>
  <div id="nav">
    
      <router-link :to="link" id="title">MEC FACTORY</router-link> 
      <p v-if="isLoggedIn" id="welcome">Welcome,  {{ popupname }}!</p>
      <router-link to="/about" id="about">About</router-link>
      <router-link to="/contact" id="about">Contact Us</router-link>
      <button v-if="isLoggedIn" @click="handleLogoutClick" class="button">Logout</button>
  
</div>
</template>

<script>
import { defineComponent, computed } from 'vue';
import { useUserStore } from '@/services/user-store';

export default defineComponent({
name: 'Navbar',
data() {
    return {
      isLoggedIn: false,
    };
  },
setup() {
  
  const userStore = useUserStore();
  const islogged =  localStorage.getItem('isLoggedIn');
  const popupname = localStorage.getItem('name');
  

  const handleLogoutClick = () => {
    userStore.logout();
    location.reload();
  };

  const link = computed(() => {
    if(islogged){
      return "/main"
    }else {return "/"}
  });

  const showButton = computed(() => {
    return islogged;
  });

  return {
   islogged,
   popupname,
   handleLogoutClick,
   link,
   showButton,
  };
},
mounted() {
    // Check the authentication state when the component is loaded
    this.isLoggedIn = localStorage.getItem('isLoggedIn');/* Check your authentication state here */;
    
  },
});
</script>


<style scoped>
.button{
background-color: #007bff;
color: #ffffff;
padding: 10px 20px;
border: none;
border-radius: 4px;
cursor: pointer;
transition: background-color 0.3s ease; 
}
.button:hover {
background-color: #0056b3;
}
#welcome
{
  margin:10px;  
  margin-left: 300px;
  color: #ffff;
  text-decoration:none;
  font-family: Noto Sans JP;
  font-size: 30px;
  background-color:#40413f ;
}
#title {
 margin:auto;
 margin-left: 0;
 color: #ffff;
 text-decoration:none;
 font-family: Noto Sans JP;
 font-size: 40px;
 background-color:#40413f ;
}
#title:hover{
  color:#000000

}


#nav {
  background-color: #40413f;
  display: flex;
  justify-content: flex-end;
  align-items:center;

}


#about { 
  margin:10px;  
  color: #ffff;
  text-decoration:none;
  font-family: Noto Sans JP;
  font-size: 30px;
  background-color:#40413f ;
}
#about:hover{
  color:#000000

}
body {
  margin: 0; /* Remove default margins */
  padding: 0; /* Remove default padding */
}
@media screen and (max-width: 768px) {
  #nav {
    flex-direction: column;
    align-items: flex-start;
    padding: 10px;
  }
  .nav-link {
    margin: 10px 0;
  }
}
</style>