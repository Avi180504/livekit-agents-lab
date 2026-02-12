# Tool-Augmented Voice Agent – Tools Used

## Overview

This project implements a real-time voice AI assistant using LiveKit Agents.

The agent uses multiple specialized tools (models and plugins) to extend its capabilities beyond basic language processing.

The system follows a modular architecture where:

Voice Input → Processing Tools → AI Reasoning → Voice Output

---

# Architecture Flow

User Speech
→ Speech-to-Text (Deepgram)
→ LLM Reasoning (OpenAI GPT-4.1-mini)
→ Text-to-Speech (Cartesia)
→ Audio Output to Room

Additional supporting tools:
- Voice Activity Detection (Silero)
- Multilingual Turn Detection
- Noise Cancellation

---

# Tools Used

## 1. Speech-to-Text (STT)

Tool:

Purpose:
- Converts user voice into text
- Supports multilingual input
- Enables real-time transcription

Why needed:
The LLM cannot process raw audio. STT converts speech into text for reasoning.

---

## 2. Large Language Model (LLM)

Tool:

Purpose:
- Interprets user intent
- Generates intelligent responses
- Maintains conversational flow

Why needed:
This acts as the reasoning engine (brain) of the assistant.

---

## 3. Text-to-Speech (TTS)

Tool:

Purpose:
- Converts generated text response into natural speech
- Delivers audio output back to the user

Why needed:
Enables full voice-based interaction instead of text-only output.

---

## 4. Voice Activity Detection (VAD)

Tool:

Purpose:
- Detects when user starts and stops speaking
- Reduces unnecessary processing
- Improves conversation timing

Why needed:
Prevents interruptions and ensures smooth turn-taking.

---

## 5. Multilingual Turn Detection

Tool:

Purpose:
- Determines when the user has finished speaking
- Manages conversational turns
- Supports multiple languages

Why needed:
Allows the agent to respond at appropriate moments in real-time conversation.

---

## 6. Noise Cancellation

Tool:

Purpose:
- Reduces background noise
- Improves audio clarity
- Enhances speech recognition accuracy

Why needed:
Improves user experience in real-world environments.

---

# Tool Invocation Flow

1. User joins LiveKit room
2. AgentServer starts session
3. Audio input received
4. VAD detects speech
5. STT converts speech to text
6. LLM generates response
7. TTS converts response to audio
8. Audio streamed back to room

---

# Agent vs Tool Responsibilities

Agent:
- Defines personality and instructions
- Coordinates session
- Manages interaction flow

Tools:
- Perform specialized tasks
- Handle speech processing
- Provide AI reasoning
- Manage audio enhancement

The agent orchestrates tools but does not perform their internal logic.

---

# Benefits of This Tool-Augmented Architecture

- Real-time voice interaction
- Modular design
- Replaceable models
- Multilingual support
- Production-ready architecture

---

# Limitations

- Requires internet connectivity
- Dependent on external model providers
- Latency depends on network quality
- Requires API keys for each model provider

---

# Conclusion

This voice AI assistant is a tool-augmented system where the agent coordinates multiple AI and signal-processing tools to enable real-time conversational voice interaction.

The architecture clearly separates:

Agent Logic → Orchestration
Tools → Specialized Processing Modules
