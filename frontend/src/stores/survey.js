import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useSurveyStore = defineStore('survey', () => {
    const activePanel = ref(1)
    const currentSurvey = ref({})
    const currentDeployment = ref({})

    function setCurrentSurvey(survey) {
        currentSurvey.value = survey
        activePanel.value++
    }

    function setCurrentDeployment(deployment) {
        currentDeployment.value = deployment
        activePanel.value++
    }

    return {
        activePanel,
        currentSurvey,
        currentDeployment,
        setCurrentSurvey,
        setCurrentDeployment,
    }
})
