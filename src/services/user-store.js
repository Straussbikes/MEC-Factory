import {defineStore} from "pinia";
import {ref} from "vue";
import axios from "axios";

export const useUserStore = defineStore("user",() => {
    const token = ref("null");
    const expiresIn = ref("null");
    const data=ref("null")
    const isLoggedIn = ref(localStorage.getItem('isLoggedIn') === 'true' || false);
    const name=ref("null");
    const tableData=[];
    const setTime =() =>{
        setTimeout(() =>{
          refreshToken()
        },expiresIn.value*1000 -6000)
      };

    const logout  = async () => {
        try {
         const email = localStorage.getItem("emaila");
         const response =await axios.get("/logout",{params:{email:email}});
         console.log(response)
        } catch (error) {
            console.log(error);
        } finally{
            resetStore();
        }
    };
     
    const refreshToken =  async () =>{
        try {
          const res = await axios.get("/refresh");
          token.value = res.data.token;
          expiresIn.value=res.data.expiresIn;
          setTime();
        } catch (error) {
          console.log(error);
        }
      };
   
    const resetStore = () =>{
         token.value = null;
         expiresIn.value=null;
         isLoggedIn.value = false;
         localStorage.removeItem('tableData')
         localStorage.removeItem('isLoggedIn');
         localStorage.removeItem('name');
         localStorage.removeItem('emaila');
         
    };
   
    return {
        tableData,
        data,
        token,
        expiresIn,
        isLoggedIn,
        name,
        setTime,
        refreshToken,
        logout,
       
        
        
    };
});