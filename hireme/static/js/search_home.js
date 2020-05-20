$( function() {
//    var availableTags = [
//      "ActionScript",
//      "AppleScript",
//      "Asp",
//      "BASIC",
//      "C",
//      "C++",
//      "Clojure",
//      "COBOL",
//      "ColdFusion",
//      "Erlang",
//      "Fortran",
//      "Groovy",
//      "Haskell",
//      "Java",
//      "JavaScript",
//      "Lisp",
//      "Perl",
//      "PHP",
//      "Python",
//      "Ruby",
//      "Scala",
//      "Scheme"
//    ];

     var availableTags = JSON.parse(document.getElementById("all_roles").value);

    $( "#search_textbox" ).autocomplete({
      source: availableTags
    });
  } );


//Vue.mixin({
//  data: function() {
//    return {
//      recent_candidates:[]
//    }
//  }
//})


//  new Vue({
//  el: '#search_box',
//  data: {
//    search_keyword: ''
//  },
//  methods: {
//    SearchResume: function(e) {
//      if (e.keyCode === 13) {
////        $.post("/employer/search_with_keyword", {
////                "search_keyword": $('#search_textbox').val()
////                }, function(response){
////                console.log(response.data)
////                    recent_candidates = response.data.recent_candidates
////              });
////
//
//          axios.post("/employer/search_with_keyword", {
//                search_keyword: $('#search_textbox').val()
//                })
//                .then(response => {
//                    recent_candidates = response.data.recent_candidates
//                    console.log(recent_candidates)
//                })
//                .catch(e => {
//                alert(e)
//                })
//
//      }
//    },
//
//}
//});


new Vue({
	el: '#main',
	data() {
  	return {
    	loading: true,
      recent_candidates: [],
      search_keyword:''
    }
  },
    methods: {
    SearchResume: function(e) {
      if (e.keyCode === 13) {

          axios.post("/employer/search_with_keyword", {
                search_keyword: $('#search_textbox').val()
                })
                .then(response => {
                    this.recent_candidates = response.data.recent_candidates
                    console.log(this.recent_candidates)
                })
                .catch(e => {
                console.log(e)
                })

      }
    },

},
  created() {
          	axios.get("/employer/load_recent_candidates").then((response) => {
                  this.recent_candidates = response.data.recent_candidates
                  console.log(this.recent_candidates[0].role)
                  this.loading = false
    })

  }
})