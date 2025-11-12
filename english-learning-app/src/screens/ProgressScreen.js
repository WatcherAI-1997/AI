import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';

export default function ProgressScreen() {
  const [stats, setStats] = useState({
    wordsLearned: 0,
    exercisesCompleted: 0,
    averageScore: 0,
    studyDays: 0,
    currentStreak: 0,
  });

  useEffect(() => {
    loadProgress();
  }, []);

  const loadProgress = async () => {
    try {
      const savedStats = await AsyncStorage.getItem('userProgress');
      if (savedStats) {
        setStats(JSON.parse(savedStats));
      }
    } catch (error) {
      console.error('Error loading progress:', error);
    }
  };

  const ProgressBar = ({ label, value, maxValue, color }) => {
    const percentage = (value / maxValue) * 100;
    return (
      <View style={styles.progressBarContainer}>
        <View style={styles.progressBarHeader}>
          <Text style={styles.progressBarLabel}>{label}</Text>
          <Text style={styles.progressBarValue}>
            {value} / {maxValue}
          </Text>
        </View>
        <View style={styles.progressBarTrack}>
          <View
            style={[
              styles.progressBarFill,
              { width: `${percentage}%`, backgroundColor: color },
            ]}
          />
        </View>
      </View>
    );
  };

  const StatCard = ({ icon, title, value, subtitle }) => (
    <View style={styles.statCard}>
      <Text style={styles.statIcon}>{icon}</Text>
      <Text style={styles.statValue}>{value}</Text>
      <Text style={styles.statTitle}>{title}</Text>
      {subtitle && <Text style={styles.statSubtitle}>{subtitle}</Text>}
    </View>
  );

  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.headerTitle}>Your Progress</Text>
        <Text style={styles.headerSubtitle}>Keep up the great work!</Text>
      </View>

      <View style={styles.statsGrid}>
        <StatCard
          icon="📚"
          title="Words Learned"
          value={stats.wordsLearned}
          subtitle="Total vocabulary"
        />
        <StatCard
          icon="✅"
          title="Exercises"
          value={stats.exercisesCompleted}
          subtitle="Completed"
        />
        <StatCard
          icon="📊"
          title="Avg Score"
          value={`${stats.averageScore}%`}
          subtitle="Quiz results"
        />
        <StatCard
          icon="🔥"
          title="Streak"
          value={`${stats.currentStreak} days`}
          subtitle="Keep going!"
        />
      </View>

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Learning Progress</Text>
        <ProgressBar
          label="Beginner Level"
          value={25}
          maxValue={50}
          color="#4CAF50"
        />
        <ProgressBar
          label="Intermediate Level"
          value={5}
          maxValue={50}
          color="#FF9800"
        />
        <ProgressBar
          label="Advanced Level"
          value={0}
          maxValue={50}
          color="#F44336"
        />
      </View>

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Achievements</Text>
        <View style={styles.achievementsList}>
          <View style={styles.achievementCard}>
            <Text style={styles.achievementIcon}>🏆</Text>
            <View style={styles.achievementInfo}>
              <Text style={styles.achievementTitle}>First Steps</Text>
              <Text style={styles.achievementDescription}>
                Complete your first exercise
              </Text>
            </View>
          </View>
          <View style={[styles.achievementCard, styles.achievementLocked]}>
            <Text style={styles.achievementIcon}>🔒</Text>
            <View style={styles.achievementInfo}>
              <Text style={styles.achievementTitle}>Word Master</Text>
              <Text style={styles.achievementDescription}>
                Learn 100 words
              </Text>
            </View>
          </View>
          <View style={[styles.achievementCard, styles.achievementLocked]}>
            <Text style={styles.achievementIcon}>🔒</Text>
            <View style={styles.achievementInfo}>
              <Text style={styles.achievementTitle}>Perfect Score</Text>
              <Text style={styles.achievementDescription}>
                Get 100% in a quiz
              </Text>
            </View>
          </View>
        </View>
      </View>

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Weekly Activity</Text>
        <View style={styles.weeklyActivity}>
          {['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'].map(
            (day, index) => (
              <View key={index} style={styles.dayColumn}>
                <View
                  style={[
                    styles.activityBar,
                    { height: Math.random() * 60 + 20 },
                  ]}
                />
                <Text style={styles.dayLabel}>{day}</Text>
              </View>
            )
          )}
        </View>
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  header: {
    backgroundColor: '#4CAF50',
    padding: 30,
    alignItems: 'center',
  },
  headerTitle: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 5,
  },
  headerSubtitle: {
    fontSize: 16,
    color: '#fff',
    opacity: 0.9,
  },
  statsGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    padding: 10,
  },
  statCard: {
    backgroundColor: '#fff',
    borderRadius: 10,
    padding: 15,
    margin: 5,
    width: '47%',
    alignItems: 'center',
    elevation: 2,
  },
  statIcon: {
    fontSize: 32,
    marginBottom: 10,
  },
  statValue: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 5,
  },
  statTitle: {
    fontSize: 14,
    color: '#666',
    marginBottom: 3,
  },
  statSubtitle: {
    fontSize: 12,
    color: '#999',
  },
  section: {
    backgroundColor: '#fff',
    margin: 10,
    borderRadius: 10,
    padding: 15,
    elevation: 2,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 15,
  },
  progressBarContainer: {
    marginBottom: 15,
  },
  progressBarHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 5,
  },
  progressBarLabel: {
    fontSize: 14,
    color: '#666',
  },
  progressBarValue: {
    fontSize: 14,
    fontWeight: 'bold',
    color: '#333',
  },
  progressBarTrack: {
    height: 10,
    backgroundColor: '#e0e0e0',
    borderRadius: 5,
    overflow: 'hidden',
  },
  progressBarFill: {
    height: '100%',
    borderRadius: 5,
  },
  achievementsList: {
    gap: 10,
  },
  achievementCard: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#E8F5E9',
    borderRadius: 10,
    padding: 15,
    marginBottom: 10,
  },
  achievementLocked: {
    backgroundColor: '#f5f5f5',
    opacity: 0.6,
  },
  achievementIcon: {
    fontSize: 32,
    marginRight: 15,
  },
  achievementInfo: {
    flex: 1,
  },
  achievementTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 3,
  },
  achievementDescription: {
    fontSize: 14,
    color: '#666',
  },
  weeklyActivity: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    alignItems: 'flex-end',
    height: 120,
  },
  dayColumn: {
    alignItems: 'center',
  },
  activityBar: {
    width: 30,
    backgroundColor: '#4CAF50',
    borderRadius: 5,
    marginBottom: 5,
  },
  dayLabel: {
    fontSize: 12,
    color: '#666',
  },
});
