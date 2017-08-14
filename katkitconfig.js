[	  
	  {
	        "EnvName": "default",
                "LocalFleet": "true", 
		"WorkFlow" : [  
					   {  
						  "Name":"BASIC",
						  "PhaseType":4,
						  "BuildParams":"PHASE=SUITE_BASIC, FOO=BAR",
						  "Order":0,
						  "Parallelism":1,
						  "ContainerImage":"duplocloud/zbuilder:selenium-v0"
					   },
					   {  
						  "Name":"ADVANCED",
						  "PhaseType":4,
						  "BuildParams":"PHASE=SUITE_ADVANCED",
						  "Order":0,
						  "Parallelism":1,
						  "ContainerImage":"duplocloud/zbuilder:selenium-v0"
					   }
					]
	  }
]

