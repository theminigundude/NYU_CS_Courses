<template>
  <div class="container">
      <h1>Classes Options for Fall 2019 NYU CS Classes</h1>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      classes: [],
    };
  },
  methods: {
    getClasses() {
      const path = 'http://localhost:5000/classes';
      axios.get(path)
        .then((res) => {
          this.classes = res.data.classes;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getBooks();
  },
};
</script>
