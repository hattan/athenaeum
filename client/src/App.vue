<template>
<div id="wrapper">
  <div id="app">
    <h1>SoCal Code Camp</h1>
    <h3>Sessions</h3>
    <ul>
     <li v-for="item in items">{{item.title}}</li>
    </ul>
    <input type="text" v-model="newSession"/>
    <button @click="addSession(newSession)">Add</button>
  </div>
  </div>
</template>

<script>
import Vue from 'vue'
export default {
  name: 'app',
  mounted: function () {
    Vue.axios.get("http://localhost:5000/api/sessions").then((response) => {
      this.items = response.data.data;
    })
  },
  data () {
    return {
      newSession: 'foo',
      items : []
    }
  },
  methods : {
    addSession : function(session){
      var payload = {'title':session};
       Vue.axios.post("http://localhost:5000/api/sessions", 
                      payload,
                      {headers: { 'Content-Type': 'application/json' }}
                      ).then((response) => {
          this.items.push(payload);
      })     
    }
  }
}
</script>

<style lang="scss">
#wrapper{
  margin-left:40%;
  margin-right:50%;
  width:500px;
  background-color:white;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
