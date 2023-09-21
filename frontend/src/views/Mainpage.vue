
<template>
  <div class="page-container">
    <div class="left-column">
      <div class="section">
        <v-table  height="300px">
          <thead>
            <tr>
              <th>AppId</th>
              <th>Request</th>
              <th>Error Code</th>
              <th>Date</th>
              <th>More</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in tableData" :key="index">
              <td>{{ item.appId }}</td>
              <td>{{ item.request }}</td>
              <td>{{ item.erro }}</td>
              <td>{{ item.date }}</td>
              <td>  
              <button
                @click="openPopupWindow(item)"
              >More</button>
              </td>
            </tr>
          </tbody>
        </v-table>
      </div>
    </div>
    <div class="section">
      <div class="section switch-section">
      <v-switch   
      v-model="switchMe" class="custom-switch"  @input="handleSwitchChange">
        <template v-slot:label >
          <h1 class="white-text">Turn On MEP</h1>
          <v-progress-circular
           
            :indeterminate="switchMe"
            size="24"
            class="loading-spinner"
          ></v-progress-circular>
        </template>
      </v-switch>
      </div>
      <div v-if="switchMe" >
        <h1 class="white-texts">Use this to connect to MEP http://0.0.0.0:8000/{{ email }}/</h1>
      </div>
      <div class="download"> 
      <v-btn @click="downloadData">Download Data</v-btn>
    </div>
    </div>  
  </div>
 

</template>

<script>

import axios from 'axios';
import {ref} from "vue";
import { useUserStore } from '@/services/user-store';

 // Import your user store

const userStore = useUserStore();


export default {

  data() {
    return {
      user:null,
      switchMe: false,
      email:localStorage.getItem("emaila"),
      tableData:[],
      
    };
  },


  mounted(){
       
    this.fetchData();
    const serializedData = JSON.stringify(this.tableData);

// Save the serialized data to local storage when the page unloads
const savedTableData = localStorage.getItem('tableData');
  if (savedTableData) {
    this.tableData = JSON.parse(savedTableData);
    console.log(this.tableData)
  }

// Define um intervalo para buscar dados a cada 5 segundos (ou o valor que desejar)
    setInterval(this.fetchData, 500); // 5000 milissegundos = 5 segundos
  },
  methods: {
    handleSwitchChange() {
      if (this.switchMe) {
        this.handleSwitchOn();
      } else {
        this.handleSwitchOff();
      }
    },
    handleSwitchOn() {
      
      console.log('Switch is ON (spinning)');
    },
    handleSwitchOff() {
      // Function to execute when the switch is turned off (not spinning)
      // Add your code here
      console.log('Switch is OFF (not spinning)');
    },

    async downloadData() {
      try {
        // Realize uma chamada ao backend para obter os dados em um formato adequado
        
        const data = JSON.stringify(this.tableData, null, 2) // Assumindo que os dados são retornados no formato apropriado

        // Crie um Blob com os dados
        const blob = new Blob([data], { type: 'application/txt' });

        // Crie uma URL temporária para o Blob
        const url = window.URL.createObjectURL(blob);

        // Crie um link de download e clique nele para iniciar o download
        const link = document.createElement('a');
        link.href = url;
        link.download = 'dados.txt';
        document.body.appendChild(link);
        link.click();

        // Libere a URL temporária e remova o link
        window.URL.revokeObjectURL(url);
        document.body.removeChild(link);
      } catch (error) {
        console.error('Erro ao fazer o download:', error);
      }
    },
    openPopupWindow(item) {
      const userStore = useUserStore();
      userStore.data=item;
      
      const routeData = this.$router.push({ name: 'more'});
    
    }, 
     async fetchData(){

      
      // Faz uma solicitação HTTP GET para buscar os dados do backend
      try {
              const response =  await axios({
                method: 'GET',
                url:'/data',
                headers:{
                  'Authorization':"Bearer " + userStore.token,
                
                },
                params: {
                     email: this.email, 
                  },
              })
             let found = false;
             const data=JSON.stringify(response.data);
           
             if(response.data != null){
                  for (let i = 0; i < this.tableData.length; i++) {
                      const compare=JSON.stringify(this.tableData[i])
                        if (compare=== data) {
                           found = true;
                           break;
                        }
                  }
                 if(!found){
                  const final=JSON.parse(data)
                  this.tableData.unshift(final)
                  localStorage.setItem('tableData', JSON.stringify(this.tableData));
                 }
             }
    
          } catch (error) {
            console.error('Error fetching data:', error);
          }
    
    }, 
    handleDirectoryChange(event) {
      // Capture the selected directory and store it in selectedDirectory
      this.selectedDirectory = event.target.files[0].webkitRelativePath;
    },
    saveData() {
      if (!this.selectedDirectory) {
        // Handle the case where no directory is selected
        return;
      }

      // You can now access the selected directory using this.selectedDirectory
      console.log("Selected directory:", this.selectedDirectory);

      // Implement your logic to save data to the selected directory here
    },
  }
};
  /*
   userStore.refreshToken();
*/
</script>





<style scoped>

.white-texts{
  display: flex;
  color: white;
  font-size:20px;
  margin-bottom:100px;
}
.page-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0px; /* Adjust the gap as needed */
  height: 100vh;
}

.left-column {
  display: flex;
  flex-direction: column;
  align-items: center; /* Center contents horizontally */
  justify-content: flex-start; /* Center contents vertically */
  height: 100%; /* Make the left column fill the entire height of its container */
  margin-top: 150px;
}



.download
{
  padding: 100px; /* Adjust the padding as needed */
  margin-top: 0px; /* Add margin to move the table down */
}

.white-text {
  color: white;
  font-size:20px;
  
}


.loading-spinner {
  /* Rotate the loading spinner when the switch is toggled (green) */
  animation: spin 1s linear infinite;
  color:white;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.section {
  padding: 20px;
}
.switch-section {
  display: flex;
  justify-content: flex-end; /* Position switch to the right */
  align-items: center; /* Center switch vertically */
  /* Add background color if needed */
  padding: 100px; /* Add padding for spacing */
}
.hide-background {
  display: flex;
  background-color: transparent !important; /* Set background to transparent */
}


.custom-table {
  height: 300px;
  border-collapse: collapse; /* Collapse borders to prevent spacing */
  width: 80%; /* Adjust the width as needed */
  border: 2px solid black; /* Add black border to the table */
}

/* Add black borders to the table and its cells */


</style>



