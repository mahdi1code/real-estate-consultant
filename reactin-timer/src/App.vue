<template>
  <div>
    <div id="app">
      <h1>OpenCode Reaction Timer</h1>
      <button @click="Start" :disabled="isPlaying">Play</button>
      <!-- <p v-if="ShowResult">Reaction : {{score}} ms</p> -->
      <Results v-if="ShowResult" :score="score"/>
    </div>
    <Block v-if="isPlaying" :delay="delay" @end="endGame"/>
    
  </div>
</template>

<script>
import Block from './components/Block.vue'
import Results from './components/Results.vue'
export default {
  name: 'App',
  components: {Block, Results},
  data () {
    return {
      delay: null,
      isPlaying: false,
      score : null,
      ShowResult : false,
    }
  },

  methods : {
    Start () {
      this.delay = 2000 + Math.random() * 5000,
      this.isPlaying = true
      this.ShowResult = false
    },
    endGame (reactionTime) {
      this.score = reactionTime
      this.isPlaying = false
      this.ShowResult = true
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #444;
  margin-top: 60px;
}

button{
  background: #efaf87;
  color: white;
  border:none;
  padding: 8px 16px;
  border-radius: 4px;
  font-size: 16px;
  letter-spacing: 1px;
  cursor: pointer;
  margin: 10px;
}

button[disabled] {
  opacity: 0.2;
  cursor: not-allowed;
}
</style>
