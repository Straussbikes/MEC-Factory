<template>
  <div class="main-container">
    <Navbar />
    <router-view />
   <Rodape />
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'
import Rodape from './components/Rodape.vue'

export default {
  components: {
    Navbar,
    Rodape,
  }
}
</script>

<style >
body, html {
  margin: 0;
  padding: 0;
}
.main-container
{ 
  display: flex;
  flex-direction: column;
  /* Fill the viewport height */
  height: 100vh;
  background-color:rgb(4, 26, 59);
  


}
</style>
