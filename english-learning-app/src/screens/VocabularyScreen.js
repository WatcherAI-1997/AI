import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  Modal,
} from 'react-native';
import { vocabularyData } from '../data/vocabulary';

export default function VocabularyScreen() {
  const [selectedLevel, setSelectedLevel] = useState('beginner');
  const [selectedWord, setSelectedWord] = useState(null);
  const [modalVisible, setModalVisible] = useState(false);

  const showWordDetails = (word) => {
    setSelectedWord(word);
    setModalVisible(true);
  };

  const closeModal = () => {
    setModalVisible(false);
    setSelectedWord(null);
  };

  return (
    <View style={styles.container}>
      <View style={styles.levelSelector}>
        <TouchableOpacity
          style={[
            styles.levelButton,
            selectedLevel === 'beginner' && styles.levelButtonActive,
          ]}
          onPress={() => setSelectedLevel('beginner')}
        >
          <Text
            style={[
              styles.levelButtonText,
              selectedLevel === 'beginner' && styles.levelButtonTextActive,
            ]}
          >
            Beginner
          </Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[
            styles.levelButton,
            selectedLevel === 'intermediate' && styles.levelButtonActive,
          ]}
          onPress={() => setSelectedLevel('intermediate')}
        >
          <Text
            style={[
              styles.levelButtonText,
              selectedLevel === 'intermediate' && styles.levelButtonTextActive,
            ]}
          >
            Intermediate
          </Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[
            styles.levelButton,
            selectedLevel === 'advanced' && styles.levelButtonActive,
          ]}
          onPress={() => setSelectedLevel('advanced')}
        >
          <Text
            style={[
              styles.levelButtonText,
              selectedLevel === 'advanced' && styles.levelButtonTextActive,
            ]}
          >
            Advanced
          </Text>
        </TouchableOpacity>
      </View>

      <ScrollView style={styles.wordList}>
        {vocabularyData[selectedLevel].map((word) => (
          <TouchableOpacity
            key={word.id}
            style={styles.wordCard}
            onPress={() => showWordDetails(word)}
          >
            <View style={styles.wordHeader}>
              <Text style={styles.englishWord}>{word.english}</Text>
              <Text style={styles.transcription}>{word.transcription}</Text>
            </View>
            <Text style={styles.russianWord}>{word.russian}</Text>
            <Text style={styles.category}>#{word.category}</Text>
          </TouchableOpacity>
        ))}
      </ScrollView>

      <Modal
        animationType="slide"
        transparent={true}
        visible={modalVisible}
        onRequestClose={closeModal}
      >
        <View style={styles.modalOverlay}>
          <View style={styles.modalContent}>
            {selectedWord && (
              <>
                <Text style={styles.modalEnglish}>{selectedWord.english}</Text>
                <Text style={styles.modalTranscription}>
                  {selectedWord.transcription}
                </Text>
                <Text style={styles.modalRussian}>{selectedWord.russian}</Text>
                <View style={styles.exampleContainer}>
                  <Text style={styles.exampleLabel}>Example:</Text>
                  <Text style={styles.exampleText}>{selectedWord.example}</Text>
                </View>
                <TouchableOpacity
                  style={styles.closeButton}
                  onPress={closeModal}
                >
                  <Text style={styles.closeButtonText}>Close</Text>
                </TouchableOpacity>
              </>
            )}
          </View>
        </View>
      </Modal>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  levelSelector: {
    flexDirection: 'row',
    padding: 10,
    backgroundColor: '#fff',
    justifyContent: 'space-around',
  },
  levelButton: {
    paddingHorizontal: 20,
    paddingVertical: 10,
    borderRadius: 20,
    backgroundColor: '#e0e0e0',
  },
  levelButtonActive: {
    backgroundColor: '#4CAF50',
  },
  levelButtonText: {
    fontSize: 14,
    color: '#666',
  },
  levelButtonTextActive: {
    color: '#fff',
    fontWeight: 'bold',
  },
  wordList: {
    flex: 1,
    padding: 15,
  },
  wordCard: {
    backgroundColor: '#fff',
    borderRadius: 10,
    padding: 15,
    marginBottom: 10,
    elevation: 2,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 1 },
    shadowOpacity: 0.1,
    shadowRadius: 2,
  },
  wordHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 5,
  },
  englishWord: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
  },
  transcription: {
    fontSize: 14,
    color: '#666',
    fontStyle: 'italic',
  },
  russianWord: {
    fontSize: 16,
    color: '#666',
    marginBottom: 5,
  },
  category: {
    fontSize: 12,
    color: '#4CAF50',
    fontWeight: 'bold',
  },
  modalOverlay: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
  },
  modalContent: {
    backgroundColor: '#fff',
    borderRadius: 20,
    padding: 30,
    width: '85%',
    maxWidth: 400,
  },
  modalEnglish: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 10,
    textAlign: 'center',
  },
  modalTranscription: {
    fontSize: 18,
    color: '#666',
    fontStyle: 'italic',
    marginBottom: 15,
    textAlign: 'center',
  },
  modalRussian: {
    fontSize: 20,
    color: '#4CAF50',
    marginBottom: 20,
    textAlign: 'center',
  },
  exampleContainer: {
    backgroundColor: '#f5f5f5',
    borderRadius: 10,
    padding: 15,
    marginBottom: 20,
  },
  exampleLabel: {
    fontSize: 14,
    fontWeight: 'bold',
    color: '#666',
    marginBottom: 5,
  },
  exampleText: {
    fontSize: 16,
    color: '#333',
    lineHeight: 22,
  },
  closeButton: {
    backgroundColor: '#4CAF50',
    borderRadius: 10,
    padding: 15,
    alignItems: 'center',
  },
  closeButtonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
});
