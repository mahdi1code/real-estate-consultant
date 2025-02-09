<template>
    <div class="Block" v-if="ShoeBlock" @click="StopTimer">Click Me</div>
</template>

<script>

export default {
    props : ['delay'],
    data () {
        return {
            ShoeBlock : false,
            timer : null,
            reactionTimer : 0,
        }
    },
    mounted () {
        console.log('componenet mounted')
        setTimeout (() => {
            this.ShoeBlock = true
            this.StartTimer()
            console.log(this.delay)
        },  this.delay)
    },
    updated () {
        console.log('componenet updated')
    },
    unmounted () {
        console.log('componenet unmounted')
    },
     methods : {
        StartTimer () {
            this.timer = setInterval(() => {
                this.reactionTimer += 10
            }, 10)
        },
        StopTimer () {
            clearInterval(this.timer)
            this.$emit('end', this.reactionTimer)
        }
     }
}
</script>

<style>

.Block{
        width: 400px;
        border-radius: 20px;
        background: green;
        color: white;
        text-align: center;
        padding: 100px 0;
        margin: 40PX auto;
    }

</style>
