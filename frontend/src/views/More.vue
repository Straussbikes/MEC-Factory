<template>
    <div class="matrix-container">
      <div class="cell">
        <p>Resposta textual: </p>
        <h1>The error {{myData.erro}} means:  {{myData.solution.replace(/'txt': /, '')}}</h1>
        
      </div>
      <div class="cell">
        <p class="titulo1">Correcao sintatica: </p>
        
        <h1 v-if="hasError(myData.newUrl)">The url you used appears to have some kind of syntax error.</h1>
        <h1 v-if="hasError(myData.newUrl)" >Do u want to say this:  "{{ myData.newUrl}}" ?</h1>
        <h1 v-else> The Url ("{{ myData.request }}")appears to be with a good syntax.</h1>
      
      </div>
      <div class="cell">
        <p>Exemplo figurativo: </p>
      </div>
      <div class="cell">
        <p>Syntax checker</p>
      <h1> The above suggestion comes from an AI syntax checker. You may know more about it by clicking this link.</h1>
    </div>
    </div>
  </template>

  <script>
  import { useUserStore } from '@/services/user-store';
  import { defineComponent, ref } from 'vue';
// Adjust the path as needed


export default defineComponent({
  setup() {
    const dataStore = useUserStore();
    
    return {
      myData: dataStore.data,
      
    
      
    };
  },
  

  methods:{

    hasError(x){
      if(x!=="0"){
        return true;
      }else{
        return false;
      }
      
    
    }
  },
});






</script>
  
  <style>

  html, body {
    height: 100%;
    margin: 0;
    overflow: hidden;
  }
  .cell h1 {
    display: flex;
    color: white;
    font-size: 20px;
    align-items: jus;
     /* Specify the desired smaller font size for h1 elements */
  }
  .cell p {
    color: white;
    font-size: 36px; /* Specify the desired larger font size for p elements with class "titulo1" */
  }
  .matrix-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr;
    gap: 30px;
    width: 100%;
    height: 100%;
    padding: 100px; /* Optional padding to create some spacing from the edges */
  }


  </style>
 
  