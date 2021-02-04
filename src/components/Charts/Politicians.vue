<template>
    <div
        class="politician"
        v-for="politician in legitPoliticians"
        :key="politician"
    >
        <a
            :href="`https://twitter.com/${politician}`"
            target="_blank"
        >
            <img :src="mentions[cleanTroll][politician].imageUrl" />
            <br />
            <span>{{ politician }}</span>
        </a>
        <span class="mentions-badge">{{ mentions[cleanTroll][politician].mentions }}</span>
    </div>
    <h1 v-if="totalMentions === 0">Ni omemb v letu 2020.</h1>
</template>

<script>
import mentions from './mentions.js';

export default {
    name: 'Politicians',
    props: {
        troll: {
            type: String,
            default: '',
        },
    },
    data() {
        return {
            mentions: mentions.mentions,
        };
    },
    computed: {
        politicians() {
            return Object.keys(this.mentions);
        },
        cleanTroll() {
            return this.troll.replace('@', '').toLowerCase();
        },
        totalMentions() {
            const total = Object.keys(
                this.mentions[this.cleanTroll]
            ).reduce(
                (acc, politician) => acc += this.mentions[this.cleanTroll][politician].mentions, 0
            );
            return total;
        },
        legitPoliticians() {
            return Object.keys(this.mentions[this.cleanTroll]).filter(
                politician => this.mentions[this.cleanTroll][politician].mentions > 0
            );
        }
    },
};
</script>

<style scoped>
.politician {
    width: 120px;
    height: 80px;
    margin-bottom: 20px;
    margin-left: 5px;
    margin-right: 5px;
    position: relative;
    transition: all cubic-bezier(0.215, 0.610, 0.355, 1) 0.4s;
}
.politician:hover {
    transform: rotate(360deg);
}
a {
    display: block;
    text-decoration: none;
}
.politician img {
    width: 60px;
    height: 60px;
    border-radius: 50%;
}
.politician span {
    font-size: 14px;
    line-height: 20px;
    color: #000000;
    font-family: acumin-pro, sans-serif;
    font-size: 16px;
    font-weight: 500;
    font-style: normal;
    letter-spacing: normal;
    line-height: 16px;
    text-align: center;
    white-space: pre-wrap;
}
span.mentions-badge {
    background-color: #f9e96f;
    display: block;
    position: absolute;
    top: 0;
    right: 22px;
    width: 25px;
    height: 25px;
    border-radius: 50%;
    font-size: 18px;
    line-height: 25px;
    font-family: 'buran_ussrregular';
    font-weight: 300;
}
</style>