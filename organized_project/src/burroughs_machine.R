# THE BURROUGHS MACHINE: A STOCHASTIC REALITY HACKER
# ---------------------------------------------------
# "When you cut into the present, the future leaks out." - W.S.B.

burroughs_machine <- function(input_text, output_length = 50, chaos_factor = 0.3) {

  # 1. CLEAN THE VIRUS (Preprocessing)
  # Remove punctuation and lower case to treat words as raw symbols
  clean_text <- tolower(input_text)
  clean_text <- gsub("[[:punct:]]", "", clean_text)
  tokens <- unlist(strsplit(clean_text, "\\s+"))
  tokens <- tokens[tokens != ""] # Remove empty tokens

  # 2. BUILD THE STATE TABLE (Markov Chain Construction)
  # Map which words follow which words in the "Control Reality"
  word_map <- list()

  for (i in 1:(length(tokens) - 1)) {
    current_word <- tokens[i]
    next_word <- tokens[i+1]

    if (is.null(word_map[[current_word]])) {
      word_map[[current_word]] <- c(next_word)
    } else {
      word_map[[current_word]] <- c(word_map[[current_word]], next_word)
    }
  }

  # 3. EXECUTE THE CUT-UP (Generation Loop)
  current_word <- sample(tokens, 1) # Start at a random point in the tape
  output_tape <- c(current_word)

  cat("--- INITIALIZING BURROUGHS MACHINE ---\n")
  cat("--- CUTTING CONTROL LINES ---\n\n")

  for (i in 1:output_length) {
    # Check if the current word exists in our map and has followers
    possible_next_steps <- word_map[[current_word]]

    # THE WILLPOWER CHECK (Chaos Logic)
    # If runif(1) < chaos_factor, we reject the script and teleport.
    # Or if we hit a dead end in the map.
    is_glitch <- runif(1) < chaos_factor
    is_dead_end <- is.null(possible_next_steps)

    if (is_glitch || is_dead_end) {
      # THE CUT: Teleport to a random point in the tape
      current_word <- sample(tokens, 1)
      # Visual marker of the cut (optional, for debugging reality)
      # output_tape <- c(output_tape, "|")
    } else {
      # THE SCRIPT: Follow the probable path (The Collective Unconscious)
      current_word <- sample(possible_next_steps, 1)
    }

    output_tape <- c(output_tape, current_word)
  }

  # 4. PROJECT THE NEW REALITY
  final_output <- paste(output_tape, collapse = " ")
  return(final_output)
}

# --- EXAMPLE USAGE ---

# The "Control Text" - A typical corporate/political deflection on climate
# control_text <- "We are committed to sustainable growth and reducing our carbon footprint while ensuring economic stability for our shareholders. The climate challenge requires innovation and global partnership to secure a green future."

# Run the machine with high chaos (30% chance to break the syntax)
# result <- burroughs_machine(control_text, output_length = 30, chaos_factor = 0.3)

# cat("\n--- OUTPUT FROM THE INTERZONE ---\n")
# cat(result)
\n\n# --- Cybernetic Burroughs Engine from climate4.md ---\n
# THE CYBERNETIC BURROUGHS ENGINE
# ---------------------------------------------------
# "The study of thinking machines teaches us more about the brain
# than the study of the brain teaches us about machines." - W.S.B.

# Install/Load necessary libraries
library(igraph)

cybernetic_willpower <- function(input_text, shift_intensity = 2.0, output_length = 60) {

  # 1. SIGNAL ACQUISITION & TOKENIZATION
  # ------------------------------------
  clean_text <- tolower(input_text)
  clean_text <- gsub("[^a-z\\s]", "", clean_text) # Keep only letters/spaces
  tokens <- unlist(strsplit(clean_text, "\\s+"))
  tokens <- tokens[tokens != ""]

  # 2. CONSTRUCT THE CONTROL MATRIX (Adjacency List)
  # ------------------------------------
  # Create a dataframe of source -> target transitions
  edges <- data.frame(
    source = tokens[1:(length(tokens)-1)],
    target = tokens[2:length(tokens)]
  )

  # Build a directed graph representing the "Collective Unconscious" of the text
  g <- graph_from_data_frame(edges, directed = TRUE)

  # 3. CRYPTOANALYSIS: IDENTIFY CONTROL POINTS
  # ------------------------------------
  # Calculate PageRank: measures the "authority" or "gravity" of a word in the system.
  # High PageRank words are the primary viral agents (e.g., "is", "the", "money", "fear").
  node_ranks <- page_rank(g)$vector

  # 4. THE WILLPOWER SHIFT (Feed-forward Injection)
  # ------------------------------------
  # We iterate through the graph. For every transition, we calculate a probability.
  # CRITICAL STEP: We *invert* the authority.
  # If a path leads to a high-ranking Control Word, we reduce its probability.
  # We boost paths leading to low-ranking (repressed) words.

  current_word <- sample(tokens, 1) # Start point
  output_tape <- c(current_word)

  cat("--- ANALYZING CONTROL TOPOLOGY ---\n")
  cat(paste("Detected Nodes:", length(V(g)), "\n"))
  cat(paste("Applying Negative Feedback Loop (Intensity:", shift_intensity, ")...\n\n"))

  for (i in 1:output_length) {
    # Get neighbors (possible next words)
    if (!current_word %in% names(V(g))) {
       current_word <- sample(names(V(g)), 1) # Reset if lost
    }

    neighbors <- neighbors(g, current_word, mode = "out")

    if (length(neighbors) == 0) {
      current_word <- sample(names(V(g)), 1) # Dead end, jump to random node
    } else {
      # Get the names of the neighbors
      neighbor_names <- names(neighbors)

      # Retrieve the "Authority Score" (PageRank) of these neighbors
      neighbor_scores <- node_ranks[neighbor_names]

      # --- THE CYBERNETIC INTERVENTION ---
      # In a normal unconscious state, we choose the highest score (habit).
      # Here, we apply Willpower: Weight = 1 / (Score ^ shift_intensity)
      # We actively punish high-frequency control words.
      weights <- 1 / (neighbor_scores ^ shift_intensity)

      # Normalize weights to probabilities
      probs <- weights / sum(weights)

      # Select next word based on the NEW Willpower distribution
      current_word <- sample(neighbor_names, 1, prob = probs)
    }

    output_tape <- c(output_tape, current_word)
  }

  return(paste(output_tape, collapse = " "))
}

# --- DEPLOYMENT ---

# A "Control Text": A generic political defense of the status quo.
# control_input <- "The economy requires constant growth to ensure stability. We must protect the market mechanisms that drive innovation. The climate situation is serious but we cannot jeopardize the financial systems that underpin our society. Order must be maintained through consumption and regulated output. The system is working as intended."

# Execute the Shift
# shift_intensity > 1 favors rare words (The Hidden Text)
# shift_intensity < 0 favors common words (The Dictator)
# result <- cybernetic_willpower(control_input, shift_intensity = 3.0, output_length = 50)

# cat("--- DECODED REALITY ---\n")
# cat(result)
