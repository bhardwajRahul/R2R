from shared.api.models.auth.responses import (
    TokenResponse,
    WrappedTokenResponse,
)
from shared.api.models.base import (
    GenericBooleanResponse,
    GenericMessageResponse,
    PaginatedR2RResult,
    R2RResults,
    WrappedBooleanResponse,
    WrappedGenericMessageResponse,
)
from shared.api.models.graph.responses import (
    GraphResponse,
    WrappedCommunitiesResponse,
    WrappedCommunityResponse,
    WrappedEntitiesResponse,
    WrappedEntityResponse,
    WrappedGraphResponse,
    WrappedGraphsResponse,
    WrappedRelationshipResponse,
    WrappedRelationshipsResponse,
)
from shared.api.models.ingestion.responses import (
    IngestionResponse,
    WrappedIngestionResponse,
    WrappedMetadataUpdateResponse,
    WrappedUpdateResponse,
    WrappedVectorIndexResponse,
    WrappedVectorIndicesResponse,
)
from shared.api.models.management.responses import (
    ChunkResponse,
    CollectionResponse,
    ConversationResponse,
    MessageResponse,
    PromptResponse,
    ServerStats,
    SettingsResponse,
    WrappedAPIKeyResponse,
    WrappedAPIKeysResponse,
    WrappedChunkResponse,
    WrappedChunksResponse,
    WrappedCollectionResponse,
    WrappedCollectionsResponse,
    WrappedConversationMessagesResponse,
    WrappedConversationResponse,
    WrappedConversationsResponse,
    WrappedDocumentResponse,
    WrappedDocumentsResponse,
    WrappedLimitsResponse,
    WrappedLoginResponse,
    WrappedMessageResponse,
    WrappedPromptResponse,
    WrappedPromptsResponse,
    WrappedServerStatsResponse,
    WrappedSettingsResponse,
    WrappedUserResponse,
    WrappedUsersResponse,
)
from shared.api.models.retrieval.responses import (
    AgentEvent,
    AgentResponse,
    AggregateSearchResult,
    Citation,
    CitationData,
    CitationEvent,
    Delta,
    DeltaPayload,
    FinalAnswerData,
    FinalAnswerEvent,
    MessageData,
    MessageDelta,
    MessageEvent,
    RAGEvent,
    RAGResponse,
    SearchResultsData,
    SearchResultsEvent,
    SSEEventBase,
    ThinkingData,
    ThinkingEvent,
    ToolCallData,
    ToolCallEvent,
    ToolResultData,
    ToolResultEvent,
    UnknownEvent,
    WrappedAgentResponse,
    WrappedDocumentSearchResponse,
    WrappedEmbeddingResponse,
    WrappedLLMChatCompletion,
    WrappedRAGResponse,
    WrappedSearchResponse,
    WrappedVectorSearchResponse,
)

__all__ = [
    # Generic Responses
    "SSEEventBase",
    "SearchResultsData",
    "SearchResultsEvent",
    "MessageDelta",
    "MessageData",
    "MessageEvent",
    "DeltaPayload",
    "Delta",
    "CitationData",
    "CitationEvent",
    "FinalAnswerData",
    "FinalAnswerEvent",
    "ToolCallData",
    "ToolCallEvent",
    "ToolResultData",
    "ToolResultEvent",
    "ThinkingData",
    "ThinkingEvent",
    "AgentEvent",
    "RAGEvent",
    "UnknownEvent",
    # Auth Responses
    "GenericMessageResponse",
    "TokenResponse",
    "WrappedTokenResponse",
    "WrappedGenericMessageResponse",
    # Ingestion Responses
    "IngestionResponse",
    "WrappedIngestionResponse",
    "WrappedUpdateResponse",
    "WrappedVectorIndexResponse",
    "WrappedVectorIndicesResponse",
    "WrappedMetadataUpdateResponse",
    "GraphResponse",
    "WrappedGraphResponse",
    "WrappedGraphsResponse",
    "WrappedEntityResponse",
    "WrappedEntitiesResponse",
    "WrappedRelationshipResponse",
    "WrappedRelationshipsResponse",
    "WrappedCommunityResponse",
    "WrappedCommunitiesResponse",
    # Management Responses
    "PromptResponse",
    "ServerStats",
    "SettingsResponse",
    "ChunkResponse",
    "CollectionResponse",
    "ConversationResponse",
    "MessageResponse",
    "WrappedServerStatsResponse",
    "WrappedSettingsResponse",
    # Document Responses
    "WrappedDocumentResponse",
    "WrappedDocumentsResponse",
    # Collection Responses
    "WrappedCollectionResponse",
    "WrappedCollectionsResponse",
    # Prompt Responses
    "WrappedPromptResponse",
    "WrappedPromptsResponse",
    # Chunk Responses
    "WrappedChunkResponse",
    "WrappedChunksResponse",
    # Conversation Responses
    "WrappedConversationMessagesResponse",
    "WrappedConversationResponse",
    "WrappedConversationsResponse",
    # User Responses
    "WrappedUserResponse",
    "WrappedAPIKeyResponse",
    "WrappedLimitsResponse",
    "WrappedAPIKeysResponse",
    "WrappedLoginResponse",
    "WrappedUsersResponse",
    "WrappedMessageResponse",
    # Base Responses
    "PaginatedR2RResult",
    "R2RResults",
    "GenericBooleanResponse",
    "GenericMessageResponse",
    "WrappedBooleanResponse",
    "WrappedGenericMessageResponse",
    # TODO: Clean up the following responses
    # Retrieval Responses
    "RAGResponse",
    "Citation",
    "WrappedRAGResponse",
    "AgentResponse",
    "AggregateSearchResult",
    "WrappedSearchResponse",
    "WrappedDocumentSearchResponse",
    "WrappedVectorSearchResponse",
    "WrappedAgentResponse",
    "WrappedLLMChatCompletion",
    "WrappedEmbeddingResponse",
]
