<template>
  <div>
    <h1>{{ title }}</h1>
    <p>WelCome...</p>
    <!-- <input type="text" ref="name">
    <button @click="HandelEvent">click</button> -->
    <Teleport to=".modals" v-if="showmodal">
      <Modal  theme="sale" @Close="ChangeModal">
        <h1>OpenCode Giveawaya!</h1>
        <p>Grab the course for half price</p>
        <template v-slot:links>
          <a href="#">Sign up</a>
          <a href="#">more info</a>
        </template>
      </Modal>
    </Teleport>

    <Teleport to=".modals" v-if="showmodalTwo">
      <Modal   @Close="ChangeModalTwo">
        <h1>Sign up for news</h1>
        <p>dont lose any news</p>
      </Modal>
    </Teleport>
    <button @click.alt="ChangeModal">ShowModal (alt) </button>
    <button @click="ChangeModalTwo">showmodalTwo </button>
  </div>
</template>

<script>
import Modal from './components/Modal.vue'
export default {
  name: 'App',
  components : {Modal},
  data () {
    return {
      // title : 'My Vue App',
      // header : 'sign up for a Giveaway',
      text : 'Grab the course for helf price',
      showmodal : false,
      showmodalTwo : false,
    }
  },
  methods : {
    HandelEvent () {
      console.log('event')
      console.log(this.$refs.name)
      this.$refs.name.classList.add('mahdi')
    },
    ChangeModal () {
      this.showmodal = !this.showmodal
    },
    ChangeModalTwo () {
      this.showmodalTwo = !this.showmodalTwo
    }
  }
}
</script>

<style>
#app, .modals {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
h3{
  color: red;
}
</style>
