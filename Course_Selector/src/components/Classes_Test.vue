<template>
<div>
  <h1 class="text-center bg_nyu_main_color text-white p-5">Class Planner for NYU CS Classes</h1>
  <br>
  <div class="container">
    <div class="row justify-content-md-center">
      <div class="col-md-6">
        <h3 class="text-center bg_nyu_main_color_light text-white p-3">Search</h3>
        <br>
        <b-col md="12" class="mb-1">
          <b-form-group label-cols-sm="2" label="Filter" class="mb-0">
            <b-input-group>
              <b-form-input v-model="filter"
              placeholder="Search by professors or classes">
              </b-form-input>
              <b-input-group-append>
                <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
              </b-input-group-append>
            </b-input-group>
          </b-form-group>
        </b-col>
        <b-row>
          <b-col md="12" class="my-3">
            <b-pagination
              v-model="currentPage"
              :total-rows="totalRows"
              :per-page="perPage"
              align="fill"
              class="my-0">
            </b-pagination>
          </b-col>
        </b-row>

        <b-table
        show-empty stacked="md"
        :items="classes"
        :fields="table_Fields"
        :current-page="currentPage"
        :per-page="perPage"
        :filter="filter"
        :sort-by.sync="sortBy"
        :sort-desc.sync="sortDesc"
        :sort-direction="sortDirection"
        @filtered="onFiltered">
          <template slot="title" slot-scope="row">
            {{ row.value }}
          </template>
          <template slot="professor" slot-scope="row">
            {{ row.value }}
          </template>
          <template slot="professor1" slot-scope="row">
            {{ row.value }}
          </template>
          <template slot="actions" slot-scope="row">
            <b-button size="sm" @click="row.toggleDetails">
              {{ row.detailsShowing ? 'Hide' : 'Show' }} Details
            </b-button>
          </template>
          <template slot="add_class" slot-scope="row">
            <b-button size="sm" @click="pushclass(row.item)">
              Add Class
            </b-button>
          </template>

          <template slot="row-details" slot-scope="row">
            <b-card>
              <ul>
                <li v-for="(value, key) in row.item" :key="key">{{ key }}: {{ value }}</li>
              </ul>
            </b-card>
          </template>
        </b-table>

      </div>
      <div class="col-md-6">
        <h3 class="text-center bg_nyu_main_color_light text-white p-3">Timetable</h3>
        <br>
        <vue-cal
        selected-date="2019-09-09"
        :disable-views="['years', 'year', 'month']"
        :time-from="8 * 60" :time-to="22 * 60"
        :events="class_list"
        hide-weekends
        editable-events hideTitleBar

        style="height: 668px;">
          <div class="noevents" slot="no-event">No Classes</div>
        </vue-cal>
      </div>
    </div>
  </div>
  <br><br>
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
      table_Fields: [
        {
          key: 'title',
          label: 'Class Name',
          sortable: true,
          sortDirection: 'desc',
        },
        {
          key: 'professor',
          label: 'Professor',
          sortable: true,
          class: 'text-center',
        },
        {
          key: 'actions',
          label: 'Details',
        },
        {
          key: 'add_class',
          label: 'Add',
        },
      ],
      totalRows: 1,
      currentPage: 1,
      perPage: 6,
      sortBy: null,
      sortDesc: false,
      sortDirection: 'asc',
      filter: null,
      colorcount: 0,
      colors: ['darkblue', 'lightgreen', 'darkred', 'lightblue', 'darkgreen', 'lightred', 'bg_nyu_main_color_light', 'orange', 'bg_nyu_main_color', 'yellow', 'leisurered'],
      classes: [],
      class_list: [
        {
          start: '2019-09-10 10:00',
          end: '2019-09-10 15:00',
          title: 'Intro to Programing',
          professor: 'temp',
          content: '',
          class: 'class_calender leisurered',
        },
      ],
    };
  },
  components: {
    VueCal,
  },
  mounted() {
    this.getClasses();
  },
  methods: {
    cal_color_tile() {
      const output = this.colors[this.colorcount];
      if (this.colorcount + 1 === this.colors.length) this.colorcount = 0;
      else this.colorcount += 1;
      return `class_calender ${output}`;
    },
    pushclass(input) {
      // safety checks
      const startTime = Object.keys(input).includes('start');
      const endTime = Object.keys(input).includes('end');
      const title = Object.keys(input).includes('title');
      const output = input;
      output.class = this.cal_color_tile();
      if (startTime && endTime && title) this.class_list.push(output);
    },
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
    getClasses() {
      const path = 'http://localhost:5000/classes';
      axios.get(path)
        .then((res) => {
          this.classes = res.data.classes;
          // for table
          this.totalRows = this.classes.length;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getClasses();
  },
};
</script>
