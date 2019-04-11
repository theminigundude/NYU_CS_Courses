<template>
  <div class="container">
      <h1>Classes Options for Fall 2019 NYU CS Classes</h1>
      <br>
      <vue-cal selected-date="2019-09-09"
      :disable-views="['years', 'year', 'month']"
      :time-from="8 * 60"
      :time-to="20 * 60"
      :events="events"
      hide-weekends
      hide-view-selector
      hideTitleBar
      disableViews>
      </vue-cal>
    </div>
</template>

<script>
import axios from 'axios';
import VueCal from 'vue-cal';
import 'vue-cal/dist/vuecal.css';
import '../assets/classes.css';

export default {
  name: 'classes_Homescreen',
  data() {
    return {
      classes: [],
      events: [
        {
          start: '2019-09-10 10:00',
          end: '2019-09-10 15:00',
          title: 'Intro to Programing',
          content: '',
          class: 'class_calender',
        },
        {
          start: '2019-09-12 10:00',
          end: '2019-09-12 15:00',
          title: 'Intro to Programing',
          content: '',
          class: 'class_calender',
        },
      ],
    };
  },
  components: {
    VueCal,
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
