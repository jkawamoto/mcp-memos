from google.api import annotations_pb2 as _annotations_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NodeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NODE_UNSPECIFIED: _ClassVar[NodeType]
    LINE_BREAK: _ClassVar[NodeType]
    PARAGRAPH: _ClassVar[NodeType]
    CODE_BLOCK: _ClassVar[NodeType]
    HEADING: _ClassVar[NodeType]
    HORIZONTAL_RULE: _ClassVar[NodeType]
    BLOCKQUOTE: _ClassVar[NodeType]
    LIST: _ClassVar[NodeType]
    ORDERED_LIST_ITEM: _ClassVar[NodeType]
    UNORDERED_LIST_ITEM: _ClassVar[NodeType]
    TASK_LIST_ITEM: _ClassVar[NodeType]
    MATH_BLOCK: _ClassVar[NodeType]
    TABLE: _ClassVar[NodeType]
    EMBEDDED_CONTENT: _ClassVar[NodeType]
    TEXT: _ClassVar[NodeType]
    BOLD: _ClassVar[NodeType]
    ITALIC: _ClassVar[NodeType]
    BOLD_ITALIC: _ClassVar[NodeType]
    CODE: _ClassVar[NodeType]
    IMAGE: _ClassVar[NodeType]
    LINK: _ClassVar[NodeType]
    AUTO_LINK: _ClassVar[NodeType]
    TAG: _ClassVar[NodeType]
    STRIKETHROUGH: _ClassVar[NodeType]
    ESCAPING_CHARACTER: _ClassVar[NodeType]
    MATH: _ClassVar[NodeType]
    HIGHLIGHT: _ClassVar[NodeType]
    SUBSCRIPT: _ClassVar[NodeType]
    SUPERSCRIPT: _ClassVar[NodeType]
    REFERENCED_CONTENT: _ClassVar[NodeType]
    SPOILER: _ClassVar[NodeType]
    HTML_ELEMENT: _ClassVar[NodeType]
NODE_UNSPECIFIED: NodeType
LINE_BREAK: NodeType
PARAGRAPH: NodeType
CODE_BLOCK: NodeType
HEADING: NodeType
HORIZONTAL_RULE: NodeType
BLOCKQUOTE: NodeType
LIST: NodeType
ORDERED_LIST_ITEM: NodeType
UNORDERED_LIST_ITEM: NodeType
TASK_LIST_ITEM: NodeType
MATH_BLOCK: NodeType
TABLE: NodeType
EMBEDDED_CONTENT: NodeType
TEXT: NodeType
BOLD: NodeType
ITALIC: NodeType
BOLD_ITALIC: NodeType
CODE: NodeType
IMAGE: NodeType
LINK: NodeType
AUTO_LINK: NodeType
TAG: NodeType
STRIKETHROUGH: NodeType
ESCAPING_CHARACTER: NodeType
MATH: NodeType
HIGHLIGHT: NodeType
SUBSCRIPT: NodeType
SUPERSCRIPT: NodeType
REFERENCED_CONTENT: NodeType
SPOILER: NodeType
HTML_ELEMENT: NodeType

class ParseMarkdownRequest(_message.Message):
    __slots__ = ("markdown",)
    MARKDOWN_FIELD_NUMBER: _ClassVar[int]
    markdown: str
    def __init__(self, markdown: _Optional[str] = ...) -> None: ...

class ParseMarkdownResponse(_message.Message):
    __slots__ = ("nodes",)
    NODES_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(self, nodes: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...) -> None: ...

class RestoreMarkdownNodesRequest(_message.Message):
    __slots__ = ("nodes",)
    NODES_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(self, nodes: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...) -> None: ...

class RestoreMarkdownNodesResponse(_message.Message):
    __slots__ = ("markdown",)
    MARKDOWN_FIELD_NUMBER: _ClassVar[int]
    markdown: str
    def __init__(self, markdown: _Optional[str] = ...) -> None: ...

class StringifyMarkdownNodesRequest(_message.Message):
    __slots__ = ("nodes",)
    NODES_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(self, nodes: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...) -> None: ...

class StringifyMarkdownNodesResponse(_message.Message):
    __slots__ = ("plain_text",)
    PLAIN_TEXT_FIELD_NUMBER: _ClassVar[int]
    plain_text: str
    def __init__(self, plain_text: _Optional[str] = ...) -> None: ...

class GetLinkMetadataRequest(_message.Message):
    __slots__ = ("link",)
    LINK_FIELD_NUMBER: _ClassVar[int]
    link: str
    def __init__(self, link: _Optional[str] = ...) -> None: ...

class LinkMetadata(_message.Message):
    __slots__ = ("title", "description", "image")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    image: str
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., image: _Optional[str] = ...) -> None: ...

class Node(_message.Message):
    __slots__ = ("type", "line_break_node", "paragraph_node", "code_block_node", "heading_node", "horizontal_rule_node", "blockquote_node", "list_node", "ordered_list_item_node", "unordered_list_item_node", "task_list_item_node", "math_block_node", "table_node", "embedded_content_node", "text_node", "bold_node", "italic_node", "bold_italic_node", "code_node", "image_node", "link_node", "auto_link_node", "tag_node", "strikethrough_node", "escaping_character_node", "math_node", "highlight_node", "subscript_node", "superscript_node", "referenced_content_node", "spoiler_node", "html_element_node")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LINE_BREAK_NODE_FIELD_NUMBER: _ClassVar[int]
    PARAGRAPH_NODE_FIELD_NUMBER: _ClassVar[int]
    CODE_BLOCK_NODE_FIELD_NUMBER: _ClassVar[int]
    HEADING_NODE_FIELD_NUMBER: _ClassVar[int]
    HORIZONTAL_RULE_NODE_FIELD_NUMBER: _ClassVar[int]
    BLOCKQUOTE_NODE_FIELD_NUMBER: _ClassVar[int]
    LIST_NODE_FIELD_NUMBER: _ClassVar[int]
    ORDERED_LIST_ITEM_NODE_FIELD_NUMBER: _ClassVar[int]
    UNORDERED_LIST_ITEM_NODE_FIELD_NUMBER: _ClassVar[int]
    TASK_LIST_ITEM_NODE_FIELD_NUMBER: _ClassVar[int]
    MATH_BLOCK_NODE_FIELD_NUMBER: _ClassVar[int]
    TABLE_NODE_FIELD_NUMBER: _ClassVar[int]
    EMBEDDED_CONTENT_NODE_FIELD_NUMBER: _ClassVar[int]
    TEXT_NODE_FIELD_NUMBER: _ClassVar[int]
    BOLD_NODE_FIELD_NUMBER: _ClassVar[int]
    ITALIC_NODE_FIELD_NUMBER: _ClassVar[int]
    BOLD_ITALIC_NODE_FIELD_NUMBER: _ClassVar[int]
    CODE_NODE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_NODE_FIELD_NUMBER: _ClassVar[int]
    LINK_NODE_FIELD_NUMBER: _ClassVar[int]
    AUTO_LINK_NODE_FIELD_NUMBER: _ClassVar[int]
    TAG_NODE_FIELD_NUMBER: _ClassVar[int]
    STRIKETHROUGH_NODE_FIELD_NUMBER: _ClassVar[int]
    ESCAPING_CHARACTER_NODE_FIELD_NUMBER: _ClassVar[int]
    MATH_NODE_FIELD_NUMBER: _ClassVar[int]
    HIGHLIGHT_NODE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPT_NODE_FIELD_NUMBER: _ClassVar[int]
    SUPERSCRIPT_NODE_FIELD_NUMBER: _ClassVar[int]
    REFERENCED_CONTENT_NODE_FIELD_NUMBER: _ClassVar[int]
    SPOILER_NODE_FIELD_NUMBER: _ClassVar[int]
    HTML_ELEMENT_NODE_FIELD_NUMBER: _ClassVar[int]
    type: NodeType
    line_break_node: LineBreakNode
    paragraph_node: ParagraphNode
    code_block_node: CodeBlockNode
    heading_node: HeadingNode
    horizontal_rule_node: HorizontalRuleNode
    blockquote_node: BlockquoteNode
    list_node: ListNode
    ordered_list_item_node: OrderedListItemNode
    unordered_list_item_node: UnorderedListItemNode
    task_list_item_node: TaskListItemNode
    math_block_node: MathBlockNode
    table_node: TableNode
    embedded_content_node: EmbeddedContentNode
    text_node: TextNode
    bold_node: BoldNode
    italic_node: ItalicNode
    bold_italic_node: BoldItalicNode
    code_node: CodeNode
    image_node: ImageNode
    link_node: LinkNode
    auto_link_node: AutoLinkNode
    tag_node: TagNode
    strikethrough_node: StrikethroughNode
    escaping_character_node: EscapingCharacterNode
    math_node: MathNode
    highlight_node: HighlightNode
    subscript_node: SubscriptNode
    superscript_node: SuperscriptNode
    referenced_content_node: ReferencedContentNode
    spoiler_node: SpoilerNode
    html_element_node: HTMLElementNode
    def __init__(self, type: _Optional[_Union[NodeType, str]] = ..., line_break_node: _Optional[_Union[LineBreakNode, _Mapping]] = ..., paragraph_node: _Optional[_Union[ParagraphNode, _Mapping]] = ..., code_block_node: _Optional[_Union[CodeBlockNode, _Mapping]] = ..., heading_node: _Optional[_Union[HeadingNode, _Mapping]] = ..., horizontal_rule_node: _Optional[_Union[HorizontalRuleNode, _Mapping]] = ..., blockquote_node: _Optional[_Union[BlockquoteNode, _Mapping]] = ..., list_node: _Optional[_Union[ListNode, _Mapping]] = ..., ordered_list_item_node: _Optional[_Union[OrderedListItemNode, _Mapping]] = ..., unordered_list_item_node: _Optional[_Union[UnorderedListItemNode, _Mapping]] = ..., task_list_item_node: _Optional[_Union[TaskListItemNode, _Mapping]] = ..., math_block_node: _Optional[_Union[MathBlockNode, _Mapping]] = ..., table_node: _Optional[_Union[TableNode, _Mapping]] = ..., embedded_content_node: _Optional[_Union[EmbeddedContentNode, _Mapping]] = ..., text_node: _Optional[_Union[TextNode, _Mapping]] = ..., bold_node: _Optional[_Union[BoldNode, _Mapping]] = ..., italic_node: _Optional[_Union[ItalicNode, _Mapping]] = ..., bold_italic_node: _Optional[_Union[BoldItalicNode, _Mapping]] = ..., code_node: _Optional[_Union[CodeNode, _Mapping]] = ..., image_node: _Optional[_Union[ImageNode, _Mapping]] = ..., link_node: _Optional[_Union[LinkNode, _Mapping]] = ..., auto_link_node: _Optional[_Union[AutoLinkNode, _Mapping]] = ..., tag_node: _Optional[_Union[TagNode, _Mapping]] = ..., strikethrough_node: _Optional[_Union[StrikethroughNode, _Mapping]] = ..., escaping_character_node: _Optional[_Union[EscapingCharacterNode, _Mapping]] = ..., math_node: _Optional[_Union[MathNode, _Mapping]] = ..., highlight_node: _Optional[_Union[HighlightNode, _Mapping]] = ..., subscript_node: _Optional[_Union[SubscriptNode, _Mapping]] = ..., superscript_node: _Optional[_Union[SuperscriptNode, _Mapping]] = ..., referenced_content_node: _Optional[_Union[ReferencedContentNode, _Mapping]] = ..., spoiler_node: _Optional[_Union[SpoilerNode, _Mapping]] = ..., html_element_node: _Optional[_Union[HTMLElementNode, _Mapping]] = ...) -> None: ...

class LineBreakNode(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ParagraphNode(_message.Message):
    __slots__ = ("children",)
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    children: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(self, children: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...) -> None: ...

class CodeBlockNode(_message.Message):
    __slots__ = ("language", "content")
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    language: str
    content: str
    def __init__(self, language: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class HeadingNode(_message.Message):
    __slots__ = ("level", "children")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    level: int
    children: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(self, level: _Optional[int] = ..., children: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...) -> None: ...

class HorizontalRuleNode(_message.Message):
    __slots__ = ("symbol",)
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    def __init__(self, symbol: _Optional[str] = ...) -> None: ...

class BlockquoteNode(_message.Message):
    __slots__ = ("children",)
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    children: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(self, children: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...) -> None: ...

class ListNode(_message.Message):
    __slots__ = ("kind", "indent", "children")
    class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KIND_UNSPECIFIED: _ClassVar[ListNode.Kind]
        ORDERED: _ClassVar[ListNode.Kind]
        UNORDERED: _ClassVar[ListNode.Kind]
        DESCRIPTION: _ClassVar[ListNode.Kind]
    KIND_UNSPECIFIED: ListNode.Kind
    ORDERED: ListNode.Kind
    UNORDERED: ListNode.Kind
    DESCRIPTION: ListNode.Kind
    KIND_FIELD_NUMBER: _ClassVar[int]
    INDENT_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    kind: ListNode.Kind
    indent: int
    children: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(self, kind: _Optional[_Union[ListNode.Kind, str]] = ..., indent: _Optional[int] = ..., children: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...) -> None: ...

class OrderedListItemNode(_message.Message):
    __slots__ = ("number", "indent", "children")
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    INDENT_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    number: str
    indent: int
    children: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(self, number: _Optional[str] = ..., indent: _Optional[int] = ..., children: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...) -> None: ...

class UnorderedListItemNode(_message.Message):
    __slots__ = ("symbol", "indent", "children")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    INDENT_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    indent: int
    children: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(self, symbol: _Optional[str] = ..., indent: _Optional[int] = ..., children: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...) -> None: ...

class TaskListItemNode(_message.Message):
    __slots__ = ("symbol", "indent", "complete", "children")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    INDENT_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    indent: int
    complete: bool
    children: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(self, symbol: _Optional[str] = ..., indent: _Optional[int] = ..., complete: bool = ..., children: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...) -> None: ...

class MathBlockNode(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: str
    def __init__(self, content: _Optional[str] = ...) -> None: ...

class TableNode(_message.Message):
    __slots__ = ("header", "delimiter", "rows")
    class Row(_message.Message):
        __slots__ = ("cells",)
        CELLS_FIELD_NUMBER: _ClassVar[int]
        cells: _containers.RepeatedCompositeFieldContainer[Node]
        def __init__(self, cells: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DELIMITER_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    header: _containers.RepeatedCompositeFieldContainer[Node]
    delimiter: _containers.RepeatedScalarFieldContainer[str]
    rows: _containers.RepeatedCompositeFieldContainer[TableNode.Row]
    def __init__(self, header: _Optional[_Iterable[_Union[Node, _Mapping]]] = ..., delimiter: _Optional[_Iterable[str]] = ..., rows: _Optional[_Iterable[_Union[TableNode.Row, _Mapping]]] = ...) -> None: ...

class EmbeddedContentNode(_message.Message):
    __slots__ = ("resource_name", "params")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    params: str
    def __init__(self, resource_name: _Optional[str] = ..., params: _Optional[str] = ...) -> None: ...

class TextNode(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: str
    def __init__(self, content: _Optional[str] = ...) -> None: ...

class BoldNode(_message.Message):
    __slots__ = ("symbol", "children")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    children: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(self, symbol: _Optional[str] = ..., children: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...) -> None: ...

class ItalicNode(_message.Message):
    __slots__ = ("symbol", "children")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    children: _containers.RepeatedCompositeFieldContainer[Node]
    def __init__(self, symbol: _Optional[str] = ..., children: _Optional[_Iterable[_Union[Node, _Mapping]]] = ...) -> None: ...

class BoldItalicNode(_message.Message):
    __slots__ = ("symbol", "content")
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    content: str
    def __init__(self, symbol: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class CodeNode(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: str
    def __init__(self, content: _Optional[str] = ...) -> None: ...

class ImageNode(_message.Message):
    __slots__ = ("alt_text", "url")
    ALT_TEXT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    alt_text: str
    url: str
    def __init__(self, alt_text: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class LinkNode(_message.Message):
    __slots__ = ("content", "url")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    content: _containers.RepeatedCompositeFieldContainer[Node]
    url: str
    def __init__(self, content: _Optional[_Iterable[_Union[Node, _Mapping]]] = ..., url: _Optional[str] = ...) -> None: ...

class AutoLinkNode(_message.Message):
    __slots__ = ("url", "is_raw_text")
    URL_FIELD_NUMBER: _ClassVar[int]
    IS_RAW_TEXT_FIELD_NUMBER: _ClassVar[int]
    url: str
    is_raw_text: bool
    def __init__(self, url: _Optional[str] = ..., is_raw_text: bool = ...) -> None: ...

class TagNode(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: str
    def __init__(self, content: _Optional[str] = ...) -> None: ...

class StrikethroughNode(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: str
    def __init__(self, content: _Optional[str] = ...) -> None: ...

class EscapingCharacterNode(_message.Message):
    __slots__ = ("symbol",)
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    symbol: str
    def __init__(self, symbol: _Optional[str] = ...) -> None: ...

class MathNode(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: str
    def __init__(self, content: _Optional[str] = ...) -> None: ...

class HighlightNode(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: str
    def __init__(self, content: _Optional[str] = ...) -> None: ...

class SubscriptNode(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: str
    def __init__(self, content: _Optional[str] = ...) -> None: ...

class SuperscriptNode(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: str
    def __init__(self, content: _Optional[str] = ...) -> None: ...

class ReferencedContentNode(_message.Message):
    __slots__ = ("resource_name", "params")
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    params: str
    def __init__(self, resource_name: _Optional[str] = ..., params: _Optional[str] = ...) -> None: ...

class SpoilerNode(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: str
    def __init__(self, content: _Optional[str] = ...) -> None: ...

class HTMLElementNode(_message.Message):
    __slots__ = ("tag_name", "attributes", "children", "is_self_closing")
    class AttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TAG_NAME_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    IS_SELF_CLOSING_FIELD_NUMBER: _ClassVar[int]
    tag_name: str
    attributes: _containers.ScalarMap[str, str]
    children: _containers.RepeatedCompositeFieldContainer[Node]
    is_self_closing: bool
    def __init__(self, tag_name: _Optional[str] = ..., attributes: _Optional[_Mapping[str, str]] = ..., children: _Optional[_Iterable[_Union[Node, _Mapping]]] = ..., is_self_closing: bool = ...) -> None: ...
