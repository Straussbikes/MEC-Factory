<template>
    <div class="matrix-container">
      <div class="cell">
        <p>Resposta textual: </p>
        <p>Item Data:{{   myData}}</p>
      
      </div>
      <div class="cell">
        <p>Correcao sintatica: </p>
       
      </div>
      <div class="cell">
        <p>Exemplo figurativo: </p>
      </div>
      <div class="cell"></div>
    </div>
  </template>

  <script>
  import { useUserStore } from '@/services/user-store';
  import { defineComponent } from 'vue';
// Adjust the path as needed


export default defineComponent({
  setup() {
    const dataStore = useUserStore();
    return {
      myData: dataStore.data,
    };
  },
});






</script>
  
  <style>
  html, body {
    height: 100%;
    margin: 0;
    overflow: hidden;
  }
  
  .matrix-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr;
    gap: 10px;
    width: 100%;
    height: 100%;
    padding: 100px; /* Optional padding to create some spacing from the edges */
  }
  

  
  .cell p {
   
    display: flex;
    color: white;
    font-size: 32;
    
  }
  </style>
 
  