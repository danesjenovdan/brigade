<template>
    <bar-custom
        :data="transformedData"
        :id="id"
        :borderColor="color"
        :fillColor="color" />
</template>

<script>
import BarCustom from './BarCustom.vue';

export default {
    name: 'NetworkBarChart',
    components: { BarCustom },
    props: {
        data: {
            required: true,
        },
        id: {
            default: 'testId',
        },
        color: {
            default: '#000000',
        },
    },
    mounted() {
        console.log(this.data);
    },
    computed: {
        transformedData() {
            let labels = [];
            let data = [];
            if (this.data.length > 0) {
                labels = this.data[0].values.map(value => value.label);
                data = this.data[0].values.map(value => value.value);
            }
            return {
                data: {
                    labels,
                    datasets: [
                        {
                            label: this.id,
                            data,
                        }
                    ]
                }
            };
        }
    },
};
</script>

<style>

</style>