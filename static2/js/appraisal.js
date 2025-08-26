document.addEventListener('DOMContentLoaded', () => {
    const selfRatingOptions = [
        { value: 'below_expectation', text: 'Below Expectation' },
        { value: 'needs_improvement', text: 'Needs Improvement' },
        { value: 'meets_expectation', text: 'Meets Expectation' },
        { value: 'exceeds_expectation', text: 'Exceeds Expectation' }
    ];

    const competencyOptions = [
        { value: 'below_expectation', text: 'Below Expectation' },
        { value: 'meets_expectation', text: 'Meets Expectation' },
        { value: 'exceeds_expectation', text: 'Exceeds Expectation' }
    ];

    const areaOfGrowthOptions = [
        { value: 'high', text: 'High' },
        { value: 'medium', text: 'Medium' },
        { value: 'low', text: 'Low' }
    ];

    const achievementOption = [
        { value: 'low', text: 'Low(M1)'},
        { value: 'medium', text: 'Medium(M2)'},
        { value: 'high', text: 'High(M3)'}
    ];

    const proficiencyOptions = [
        { value: 'low', text: 'Low(P1)'},
        { value: 'medium', text: 'Medium(P2)'},
        { value: 'high', text: 'High(P3)'}
    ]

    const promotionOptions = [
        { value: 'yes', text: 'Yes'},
        { value: 'no', text: 'No'}
    ]

    const ttrbscoreOptions = [
        { value: 'developing', text: 'Developing'},
        { value: 'credible', text: 'Credible'},
        { value: 'amazing', text: 'Amazing'}
    ]

    const behaviorOptions = [
        {value: 'communication', text: 'Communication'},
        {value: 'collaboration', text: 'Collaboration'},
        {value: ' problem Solving ', text: 'Problem Solving '},
        {value: ' organisation and planning', text: ' Organisation and Planning'},
        {value: 'people management', text: 'People Management'},
        {value: 'personal accountability and delivery', text: 'Personal Accountability and Delivery'},
        {value: 'stakeholder management', text: 'Stakeholder Management'},
        {value: 'decision making', text: 'Decision Making'},
        {value: 'other behavioural skills', text: 'Other Behavioural Skills'},
    ]
    const technicalOptions = [
        {value: 'analysis, research and reporting', text: 'Analysis, Research and Reporting'},
        {value: 'strategy', text: 'Strategy'},
        {value: 'core areas/foundation skills', text: 'Core Areas/Foundation Skills'},
        {value: 'corporate strategy', text: 'Corporate Strategy'},
        {value: 'digital /IT', text: 'Digital /IT'},
        {value: 'finance', text: 'Finance'},
        {value: 'HR', text: 'HR'},
        {value: 'customer centrism', text: 'Customer Centrism'},
        {value: 'manufacturing & quality', text: 'Manufacturing & Quality'},
        {value: 'supply chain management', text: 'Supply Chain Management'},
        {value: 'sales & marketing', text: 'Sales & Marketing'},
        {value: 'health and safety', text: 'Health and Safety'},
        {value: 'other professional skills', text: 'Other Professional Skills'},
    ]

    const DateOptions = [
        {value: 'h1', text: 'H1'},
        {value: 'h2', text: 'H2'},

    ]
    const  employeeOptions = []
    fetch("/employee_appraisal/employee-list/")
        .then(response => response.json())
        .then(data => {
            employees = data.employees;
            for(let i = 0; i<employees.length; i++){
                employeeOptions.push(
                    {value: employees[i]["id"], text:employees[i]["name"]}
                )
            }
        })
        .catch(error => console.error("Error fetching products:", error));
    
    document.querySelectorAll('.behaviourOwner').forEach((button) => {
        button.addEventListener('click', () => {
            const parent = button.closest('h6');
            const behaviourOwnerText = parent.querySelector('[data-behaviourOwner]');
            
            createSelectionField(parent, behaviourOwnerText, 'behavioural_owner', 'data-behaviourOwner', employeeOptions)
                
        });
    });

    document.querySelectorAll('.technicalOwner').forEach((button) => {
        button.addEventListener('click', () => {
            const parent = button.closest('h6');
            const technicalOwnerText = parent.querySelector('[data-technicalOwner]');
            
            createSelectionField(parent, technicalOwnerText, 'technical_owner', 'data-technicalOwner', employeeOptions)
                
        });
    });


    document.querySelectorAll('.startDate').forEach((button) => {
        button.addEventListener('click', () => {
            const parent = button.closest('h6');
            const startDateText = parent.querySelector('[data-startDate]');
            
            createSelectionField(parent, startDateText, 'start_date', 'data-startDate', DateOptions)
              
        });
    });

    document.querySelectorAll('.endDate').forEach((button) => {
        button.addEventListener('click', () => {
            const parent = button.closest('h6');
            const endDateText = parent.querySelector('[data-endDate]');
            
            createSelectionField(parent, endDateText, 'end_date', 'data-endDate', DateOptions)
              
        });
    });

    document.querySelectorAll('.behavioural').forEach((button) => {
        button.addEventListener('click', () => {
            const parent = button.closest('h6');
            const behaviouralText = parent.querySelector('[data-behavioural]');
            
            createSelectionField(parent, behaviouralText, 'behavioural', 'data-behavioural', behaviorOptions)
              
        });
    });

    document.querySelectorAll('.technical').forEach((button) => {
        button.addEventListener('click', () => {
            const parent = button.closest('h6');
            const technicalText = parent.querySelector('[data-technical]');
            
            createSelectionField(parent, technicalText, 'technical', 'data-technical', technicalOptions)
              
        });
    });
    
    document.querySelectorAll('.edit-weightage').forEach((button) => {
        
        button.addEventListener('click', () => {
            const parent = button.closest('h6');
            const weightageText = parent.querySelector('[data-weightage]');
           
            createInputField(parent,weightageText, 'weightage', 'data-weightage')
            
        });
        
    });

    document.querySelectorAll('.edit-target').forEach((button) => {
        button.addEventListener('click', () => {
            const parent = button.closest('h6');
            const targetText = parent.querySelector('[data-target]');
           
            createInputField(parent,targetText, 'target', 'data-target')
            
        });
        
    });

    document.querySelectorAll('.edit-actual').forEach((button) => {
        button.addEventListener('click', () => {
            const parent = button.closest('h6');
            const actualText = parent.querySelector('[data-actual]');
           
            createInputField(parent,actualText, 'actual', 'data-actual')
            
        });
        
    });

    document.querySelectorAll('.edit-actual-description').forEach((button) => {
        button.addEventListener('click', () => {
            const parent = button.closest('h6');
            const actualdescText = parent.querySelector('[data-desc]');

            createInputField(parent,actualdescText, 'actual-desc', 'data-desc')
              
        });
    });

    document.querySelectorAll('.edit-dept-goal').forEach((button) => {
        button.addEventListener('click', () => {
            const parent = button.closest('h6');
            const deptGoalsText = parent.querySelector('[data-goal]');

            createInputField(parent, deptGoalsText, 'dept-goal', 'data-goal')
              
        });
    });

    document.querySelectorAll('.self-rating').forEach((button) => {
        button.addEventListener('click', () => {
            const parent = button.closest('h6');
            const selfRatingText = parent.querySelector('[data-self-rating]');
            
            createSelectionField(parent, selfRatingText, 'self-rating', 'data-self-rating', selfRatingOptions)
              
        });
    });

    document.querySelectorAll('.manager-rating').forEach((button) => {
        button.addEventListener('click', () => {
            const parent = button.closest('h6');
            const managerRatingText = parent.querySelector('[data-manager-rating]');
            
            createSelectionField(parent, managerRatingText, 'manager-rating', 'data-manager-rating', selfRatingOptions)
              
        });
    });

    document.querySelectorAll('.progress-update').forEach((button) => {
        button.addEventListener('click', () => {
            const parent = button.closest('h6');
            const progressUpdateText = parent.querySelector('[data-progress-update]');
            createInputField(parent, progressUpdateText, 'progress-update', 'data-progress-update')  
        });
    });

    document.querySelectorAll('.accomplishments').forEach((button) => {
        button.addEventListener('click', () => {
            
            const parent = button.closest('h6');
            const accomplishmentsText = parent.querySelector('[data-accomplishments]');
            
            createTextAreaField(parent, accomplishmentsText, 'accomplishments', 'data-accomplishments')
              
        });
    });

    

    document.querySelectorAll('.areas-of-growth').forEach((button) => {
        button.addEventListener('click', () => {
            const parent = button.closest('h6');
            const growthText = parent.querySelector('[data-growth]');
            
            createInputField(parent,growthText, 'growth-area', 'data-growth')
            
        });
        
    });

    document.querySelectorAll('.killing-it-like').forEach((button) => {
        button.addEventListener('click', () => {
            
            const parent = button.closest('h6');
            const killingItText = parent.querySelector('[data-killing-it]');
            
            createInputField(parent, killingItText, 'killing-it', 'data-killing-it')
              
        });
    });

    document.querySelectorAll('.stakeholder-feedback-class').forEach((button) => {
        button.addEventListener('click', () => {

            const parent = button.closest('h6');
            const stakeholderFeedback = parent.querySelector('[data-stakeholder-feedback]');
           
            createTextAreaField(parent, stakeholderFeedback, 'stakeholder-feedback', 'data-stakeholder-feedback')
              
        });
    });

    document.querySelectorAll('.manager-feedback').forEach((button) => {
        button.addEventListener('click', () => {
            
            const parent = button.closest('h6');
            const managerFeedback = parent.querySelector('[data-manager-feedback]');
           
            
            createTextAreaField(parent, managerFeedback, 'manager-feedback', 'data-manager-feedback')
              
        });
    });

    document.querySelectorAll('.promotion-class').forEach((button) => {
        button.addEventListener('click', () => {
            const parent = button.closest('h6');
            const promotionText = parent.querySelector('[data-promotion]');
            
            createSelectionField(parent, promotionText, 'promotion', 'data-promotion', promotionOptions);
            
            // Add change event listener to handle justification visibility
            const selectField = parent.querySelector('select');
            if (selectField) {
                // Function to handle visibility
                const handleJustificationVisibility = (value) => {
                    const justificationSection = document.querySelector('.justification-section');
                    if (justificationSection) {
                        if (value === 'yes') {
                            justificationSection.style.display = 'block';
                        } else {
                            justificationSection.style.display = 'none';
                            // Clear justification value when hidden
                            const justificationInput = justificationSection.querySelector('input, textarea');
                            if (justificationInput) {
                                justificationInput.value = '';
                            }
                        }
                    }
                };

                // Add change event listener
                selectField.addEventListener('change', (e) => {
                    handleJustificationVisibility(e.target.value);
                });
                
                // Set initial visibility based on current value
                const initialValue = selectField.value;
                handleJustificationVisibility(initialValue);
            }
        });
    });

    document.querySelectorAll('.justification-class').forEach((button) => {
        button.addEventListener('click', () => {
            
            const parent = button.closest('h6');
            const justificationText = parent.querySelector('[data-justification]');
           
            
            createInputField(parent, justificationText, 'justification', 'data-justification')
              
        });
    });

    document.querySelectorAll('.quantity-of-work-class').forEach((button) => {
        button.addEventListener('click', () => {
            const parent = button.closest('h6');
            const quantityText = parent.querySelector('[data-quantity-of-work]');
            
            createSelectionField(parent, quantityText, 'quantity-of-work', 'data-quantity-of-work', competencyOptions)
            
              
        });
    });

    document.querySelectorAll('.quality-of-work-class').forEach((button) => {
        button.addEventListener('click', () => {
            const parent = button.closest('h6');
            const qualityText = parent.querySelector('[data-quality]');
            
            createSelectionField(parent, qualityText, 'quality', 'data-quality', competencyOptions)
              
        });
    });
 

    document.querySelectorAll('.knowledge-of-work').forEach((button) => {
        button.addEventListener('click', () => {
            const parent = button.closest('h6');
            const knowledgeText = parent.querySelector('[data-knowledge]');
            
            createSelectionField(parent, knowledgeText, 'knowledge', 'data-knowledge', competencyOptions)
              
        });
    });


    document.querySelectorAll('.response-to-feedback').forEach((button) => {
        button.addEventListener('click', () => {
            const parent = button.closest('h6');
            const feedbackText = parent.querySelector('[data-feedback]');
            
            createSelectionField(parent, feedbackText, 'feedback', 'data-feedback', competencyOptions)
              
        });
    });

    document.querySelectorAll('.teamwork-and-collaboration').forEach((button) => {
        button.addEventListener('click', () => {
            const parent = button.closest('h6');
            const teamWorkCollaborationText = parent.querySelector('[data-team-work-collaboration]');
            
            createSelectionField(parent, teamWorkCollaborationText, 'team-work', 'data-team-work-collaboration', competencyOptions)
              
        });
    });

    document.querySelectorAll('.attendance-reliability').forEach((button) => {
        button.addEventListener('click', () => {
            const parent = button.closest('h6');
            const attendanceReliabilityText = parent.querySelector('[data-attendance-reliability]');
            
            createSelectionField(parent, attendanceReliabilityText, 'attendance-reliability', 'data-attendance-reliability', competencyOptions)
              
        });
    });

    document.querySelectorAll('.initiative-creativity').forEach((button) => {
        button.addEventListener('click', () => {
            const parent = button.closest('h6');
            const initiativeCreativityText = parent.querySelector('[data-initiative-creativity]');
            
            createSelectionField(parent, initiativeCreativityText, 'initiative-creativity', 'data-initiative-creativity', competencyOptions)
              
        });
    });

    document.querySelectorAll('.eagerness-to-grow').forEach((button) => {
        button.addEventListener('click', () => {
            const parent = button.closest('h6');
            const eagernessToGrowText = parent.querySelector('[data-eagerness-to-grow]');
            
            
            createSelectionField(parent, eagernessToGrowText, 'eagerness-to-grow', 'data-eagerness-to-grow', competencyOptions)
              
        });
    });

    
    document.querySelectorAll('.area_of_growth_mgr_feedback').forEach((button) => {
        button.addEventListener('click', () => {
            
            const parent = button.closest('h6');
            const areaOfGrowthMgrFeedbackText = parent.querySelector('[data-area_of_growth_mgr_feedback]');
            
            createInputField(parent, areaOfGrowthMgrFeedbackText, 'area_of_growth_mgr_feedback', 'data-area_of_growth_mgr_feedback')
              
        });
    });

    document.querySelectorAll('.achievement-motivation').forEach((button) => {
        button.addEventListener('click', () => {
            const parent = button.closest('h6');
            const achievementMotivationText = parent.querySelector('[data-achievement-motivation]');
            
            createSelectionField(parent, achievementMotivationText, 'achievement-motivation', 'data-achievement-motivation', areaOfGrowthOptions)
              
        });
    });

  

    document.querySelectorAll('.proficiency').forEach((button) => {
        button.addEventListener('click', () => {
           
            const parent = button.closest('h6');
            const proficiencyText = parent.querySelector('[data-proficiency]');
            createInputField(parent, proficiencyText, 'proficiency', 'data-proficiency')
              
        });
    });

    document.querySelectorAll('.proficiency-score').forEach((button) => {
        button.addEventListener('click', () => {
            const parent = button.closest('h6');
            const proficiencyScoreText = parent.querySelector('[data-proficiency-score]');
            
            createSelectionField(parent, proficiencyScoreText, 'proficiency-score', 'data-proficiency-score', areaOfGrowthOptions)
              
        });
    });

    document.querySelectorAll('.achievement-motivation').forEach((button) => {
        button.addEventListener('click', () => {
            const parent = button.closest('h6');
            const achievementMotivationText = parent.querySelector('[data-achievement-motivation]');
            
            createSelectionField(parent, achievementMotivationText, 'achievement-motivation', 'data-achievement-motivation', achievementOption)
              
        });
    });

    document.querySelectorAll('.proficiency').forEach((button) => {
        button.addEventListener('click', () => {
            const parent = button.closest('h6');
            const proficiencyText = parent.querySelector('[data-proficiency]');
            
            createSelectionField(parent, proficiencyText, 'proficiency', 'data-proficiency', proficiencyOptions)
              
        });
    });

    document.querySelectorAll('.ttrbscore').forEach((button) => {
        button.addEventListener('click', () => {
            const parent = button.closest('h6');
            const ttrbscoreText = parent.querySelector('[data-ttrbscore]');
            
            createSelectionField(parent, ttrbscoreText, 'ttrbscore', 'data-ttrbscore', ttrbscoreOptions)
              
        });
    });

    function createSelectionField(parent, dataContent, fieldName, dataGoal, options) {
        console.log('Creating selection field:', { parent, dataContent, fieldName, dataGoal, options });
        
        if (dataContent) {
            // Get the current value and ensure it's a string
            const currentValue = String(dataContent.value || dataContent.getAttribute(dataGoal) || '').trim().toLowerCase();
            console.log('Current value:', currentValue);
            
            const selectField = document.createElement('select');
            selectField.name = fieldName;
            selectField.className = 'form-control';
            selectField.style.width = '500px';

            // Always add a default empty option
            const defaultOption = document.createElement('option');
            defaultOption.value = '';
            defaultOption.textContent = 'Select an option';
            defaultOption.selected = !currentValue; // Select only if no current value
            selectField.appendChild(defaultOption);

            // Add options
            options.forEach(option => {
                const optionElement = document.createElement('option');
                // Ensure both value and text are strings
                optionElement.value = String(option.value);
                optionElement.textContent = String(option.text);
                
                if (currentValue) {
                    const optionValue = String(option.value).toLowerCase();
                    const optionText = String(option.text).toLowerCase();
                    
                    if (optionValue === currentValue || optionText === currentValue) {
                        optionElement.selected = true;
                        defaultOption.selected = false;
                    }
                }
                selectField.appendChild(optionElement);
            });

            // If no option was selected and we have a current value, try to find a match by partial text
            if (currentValue && !selectField.value) {
                const options = selectField.options;
                for (let i = 0; i < options.length; i++) {
                    const optionValue = String(options[i].value).toLowerCase();
                    const optionText = String(options[i].text).toLowerCase();
                    
                    if (optionText.includes(currentValue) || optionValue.includes(currentValue)) {
                        options[i].selected = true;
                        defaultOption.selected = false;
                        break;
                    }
                }
            }

            const container = document.createElement('div');
            container.style.display = 'inline-flex';
            container.style.alignItems = 'center';
            container.style.gap = '10px';

            container.appendChild(selectField);
            parent.innerHTML = '';
            parent.appendChild(container);

            // Add change event listener to log selections
            selectField.addEventListener('change', (e) => {
                console.log('Selection changed:', e.target.value);
            });
        } else {
            console.error('No data content found for selection field');
        }
    }
    
    
    function createInputField(parent, dataContent, fieldName, dataGoal) {
        if (dataContent) {
            // Get the current value from either the input's value or its data attribute
            const currentValue = dataContent.value || dataContent.getAttribute(dataGoal) || '';
            console.log('Creating input field with value:', currentValue);
            
            const inputField = document.createElement('input');
            inputField.name = fieldName;
            inputField.type = 'text';
            inputField.value = currentValue;
            inputField.className = 'form-control';
            inputField.style.width = '500px';
            // Store the original value in a data attribute for persistence
            inputField.setAttribute('data-original-value', currentValue);

            const container = document.createElement('div');
            container.style.display = 'inline-flex';
            container.style.alignItems = 'center';
            container.style.gap = '10px';

            container.appendChild(inputField);
            parent.innerHTML = '';
            parent.appendChild(container);

            // Add change event listener to update the data attribute
            inputField.addEventListener('change', (e) => {
                console.log('Input changed:', e.target.value);
                e.target.setAttribute('data-original-value', e.target.value);
            });
        } else {
            console.error('No data content found for input field');
        }
    }
    
    function createTextAreaField(parent, dataContent, fieldName, dataGoal) {
        if (dataContent) {
            // Get the current value from either the textarea's value or its data attribute
            const currentValue = dataContent.value || dataContent.getAttribute(dataGoal) || '';
            console.log('Creating textarea with value:', currentValue);
            
            const inputField = document.createElement('textarea');
            inputField.name = fieldName;
            inputField.value = currentValue;
            inputField.className = 'form-control';
            inputField.style.width = '500px';
            // Store the original value in a data attribute for persistence
            inputField.setAttribute('data-original-value', currentValue);

            const container = document.createElement('div');
            container.style.display = 'inline-flex';
            container.style.alignItems = 'center';
            container.style.gap = '10px';

            container.appendChild(inputField);
            parent.innerHTML = '';
            parent.appendChild(container);

            // Add change event listener to update the data attribute
            inputField.addEventListener('change', (e) => {
                console.log('Textarea changed:', e.target.value);
                e.target.setAttribute('data-original-value', e.target.value);
            });
        } else {
            console.error('No data content found for textarea field');
        }
    }
    
    document.getElementById('appraisal-submit').addEventListener('click', (event) => {
        event.preventDefault(); // Prevent form submission for debugging
        
        
        // Corrected variable name
        const lineItemElements = document.querySelectorAll('.line-item');
        
        // Extract their values into an array
        const lineItemValues = Array.from(lineItemElements).map(input => ({
            name: input.name,
            value: input.value,
        }));
        
        
        
       // Add a hidden input to the form to send this data
       const form = document.getElementById('employeeDetailsForm');
       let hiddenInput = form.querySelector('input[name="line-items"]');
       
       if (!hiddenInput) {
           hiddenInput = document.createElement('input');
           hiddenInput.type = 'hidden';
           hiddenInput.name = 'line-items';
           form.appendChild(hiddenInput);
       }
       
       hiddenInput.value = JSON.stringify(lineItemValues);

       // Submit the form after adding the hidden input
       form.submit();

       
    });

    
   

    
});
    
