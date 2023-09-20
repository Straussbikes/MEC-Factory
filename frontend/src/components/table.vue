<template>
    <div >
        <template>
            <v-container>
              <v-row>
                <v-col cols="6">
                  <v-card>
                    <v-card-title>Table</v-card-title>
                    <v-card-text>
                      <v-simple-table>
                        <template v-slot:default>
                          <thead>
                            <tr>
                              <th>ID</th>
                              <th>Name</th>
                              <th>Email</th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr v-for="item in tableData" :key="item.id">
                              <td>{{ item.id }}</td>
                              <td>{{ item.name }}</td>
                              <td>{{ item.email }}</td>
                            </tr>
                          </tbody>
                        </template>
                      </v-simple-table>
                    </v-card-text>
                  </v-card>
                </v-col>
                <v-col cols="6">
                  <v-card>
                    <v-card-title>Toggle Button</v-card-title>
                    <v-card-text>
                      <v-switch v-model="toggleValue" :color="toggleValue ? 'green' : 'red'"></v-switch>
                    </v-card-text>
                  </v-card>
                </v-col>
              </v-row>
            </v-container>
          </template>
    </div>
</template>


<script>
export default { 
  name: 'Table',
  components: {
    'butao' :Buttons
   
  }
 
}
</script>