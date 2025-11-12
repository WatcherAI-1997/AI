import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  Alert,
  ScrollView,
} from 'react-native';
import { vocabularyData } from '../data/vocabulary';

export default function ExercisesScreen() {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [score, setScore] = useState(0);
  const [questions, setQuestions] = useState([]);
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [showResult, setShowResult] = useState(false);

  useEffect(() => {
    generateQuestions();
  }, []);

  const generateQuestions = () => {
    const allWords = [
      ...vocabularyData.beginner,
      ...vocabularyData.intermediate,
      ...vocabularyData.advanced,
    ];

    const shuffled = allWords.sort(() => 0.5 - Math.random());
    const selected = shuffled.slice(0, 10);

    const generatedQuestions = selected.map((word) => {
      const wrongAnswers = allWords
        .filter((w) => w.id !== word.id)
        .sort(() => 0.5 - Math.random())
        .slice(0, 3)
        .map((w) => w.russian);

      const answers = [word.russian, ...wrongAnswers].sort(
        () => 0.5 - Math.random()
      );

      return {
        question: `What is the Russian translation of "${word.english}"?`,
        correctAnswer: word.russian,
        answers: answers,
        word: word,
      };
    });

    setQuestions(generatedQuestions);
    setCurrentQuestion(0);
    setScore(0);
    setShowResult(false);
  };

  const handleAnswer = (answer) => {
    setSelectedAnswer(answer);

    setTimeout(() => {
      if (answer === questions[currentQuestion].correctAnswer) {
        setScore(score + 1);
      }

      if (currentQuestion + 1 < questions.length) {
        setCurrentQuestion(currentQuestion + 1);
        setSelectedAnswer(null);
      } else {
        setShowResult(true);
      }
    }, 1000);
  };

  const restartQuiz = () => {
    generateQuestions();
  };

  if (questions.length === 0) {
    return (
      <View style={styles.container}>
        <Text>Loading...</Text>
      </View>
    );
  }

  if (showResult) {
    return (
      <View style={styles.container}>
        <View style={styles.resultContainer}>
          <Text style={styles.resultTitle}>Quiz Completed!</Text>
          <Text style={styles.resultScore}>
            Your Score: {score} / {questions.length}
          </Text>
          <Text style={styles.resultPercentage}>
            {Math.round((score / questions.length) * 100)}%
          </Text>
          <TouchableOpacity style={styles.restartButton} onPress={restartQuiz}>
            <Text style={styles.restartButtonText}>Try Again</Text>
          </TouchableOpacity>
        </View>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.progressText}>
          Question {currentQuestion + 1} / {questions.length}
        </Text>
        <Text style={styles.scoreText}>Score: {score}</Text>
      </View>

      <ScrollView style={styles.content}>
        <View style={styles.questionContainer}>
          <Text style={styles.questionText}>
            {questions[currentQuestion].question}
          </Text>
          <Text style={styles.transcriptionText}>
            {questions[currentQuestion].word.transcription}
          </Text>
        </View>

        <View style={styles.answersContainer}>
          {questions[currentQuestion].answers.map((answer, index) => {
            let buttonStyle = styles.answerButton;
            if (selectedAnswer) {
              if (answer === questions[currentQuestion].correctAnswer) {
                buttonStyle = [styles.answerButton, styles.correctAnswer];
              } else if (answer === selectedAnswer) {
                buttonStyle = [styles.answerButton, styles.wrongAnswer];
              }
            }

            return (
              <TouchableOpacity
                key={index}
                style={buttonStyle}
                onPress={() => handleAnswer(answer)}
                disabled={selectedAnswer !== null}
              >
                <Text style={styles.answerText}>{answer}</Text>
              </TouchableOpacity>
            );
          })}
        </View>

        <View style={styles.hintContainer}>
          <Text style={styles.hintLabel}>Example:</Text>
          <Text style={styles.hintText}>
            {questions[currentQuestion].word.example}
          </Text>
        </View>
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  header: {
    backgroundColor: '#fff',
    padding: 15,
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    borderBottomWidth: 1,
    borderBottomColor: '#e0e0e0',
  },
  progressText: {
    fontSize: 16,
    color: '#666',
  },
  scoreText: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#4CAF50',
  },
  content: {
    flex: 1,
    padding: 15,
  },
  questionContainer: {
    backgroundColor: '#fff',
    borderRadius: 10,
    padding: 20,
    marginBottom: 20,
    elevation: 3,
  },
  questionText: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 10,
    textAlign: 'center',
  },
  transcriptionText: {
    fontSize: 16,
    color: '#666',
    fontStyle: 'italic',
    textAlign: 'center',
  },
  answersContainer: {
    marginBottom: 20,
  },
  answerButton: {
    backgroundColor: '#fff',
    borderRadius: 10,
    padding: 15,
    marginBottom: 10,
    elevation: 2,
    borderWidth: 2,
    borderColor: '#e0e0e0',
  },
  correctAnswer: {
    backgroundColor: '#C8E6C9',
    borderColor: '#4CAF50',
  },
  wrongAnswer: {
    backgroundColor: '#FFCDD2',
    borderColor: '#F44336',
  },
  answerText: {
    fontSize: 16,
    color: '#333',
    textAlign: 'center',
  },
  hintContainer: {
    backgroundColor: '#E3F2FD',
    borderRadius: 10,
    padding: 15,
  },
  hintLabel: {
    fontSize: 14,
    fontWeight: 'bold',
    color: '#1976D2',
    marginBottom: 5,
  },
  hintText: {
    fontSize: 14,
    color: '#1565C0',
    lineHeight: 20,
  },
  resultContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  resultTitle: {
    fontSize: 32,
    fontWeight: 'bold',
    color: '#4CAF50',
    marginBottom: 20,
  },
  resultScore: {
    fontSize: 24,
    color: '#333',
    marginBottom: 10,
  },
  resultPercentage: {
    fontSize: 48,
    fontWeight: 'bold',
    color: '#4CAF50',
    marginBottom: 30,
  },
  restartButton: {
    backgroundColor: '#4CAF50',
    borderRadius: 10,
    paddingHorizontal: 40,
    paddingVertical: 15,
  },
  restartButtonText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: 'bold',
  },
});
