<template>
    <div class="backdrop" @click.self="CloseModal">
        <div class="modal" :class="{sale : theme == 'sale'}">
            <!-- <h2>{{header}}</h2>
            <p>{{text}}</p> -->
            <slot></slot>
            <div class="actions">
                <slot name="links"></slot>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props : ['header', 'text', 'theme'],
    methods : {
        CloseModal () {
            this.$emit ('Close')
        }
    }
}
</script>


<style >
.modal {
    width: 400px;
    padding: 20px;
    margin: 100px auto;
    background: white;
    border-radius: 10px;   
}

.backdrop {
    top: 0;
    position:fixed;
    background: rgba(0, 0, 0, 0.5);
    width: 100%;
    height: 100%;
}
.modal h3 {
    color: rgb(160, 196, 3);

}

.sale {
    background: crimson;
    color: aliceblue;
}

.sale h2 {
    color: whitesmoke;
}

.modal .actions {
    text-align: center;
    margin: 30px 0 10px 0;
}

.modal .actions a{
    color: #333;
    padding: 8px;
    border:1px solid #eee;
    border-radius: 4px;
    text-decoration: none;
    margin: 10px;
}

.sale .actions {
    color: whitesmoke;    
}

.sale .actions a {
    color: white;
}

</style>
