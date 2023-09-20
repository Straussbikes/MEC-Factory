
    <template>
        <div class="responsive-page">
          <div class="content">
            <h1>Responsive Vue Page</h1>
            <p>This page adjusts based on the browser's size.</p>
          </div>
        </div>
      </template>
      
  
       


<script>
export default {
    
}
</script>


<style scoped>
.responsive-page {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f0f0f0;
}

.content {
  text-align: center;
  padding: 20px;
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  width: 80%;
  max-width: 800px;
}
</style>