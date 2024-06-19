/*! For license information please see 9579.4b1b079b6b7cd2924338.js.LICENSE.txt */
"use strict";(self["webpackChunk_jupyterlab_application_top"]=self["webpackChunk_jupyterlab_application_top"]||[]).push([[9579],{29579:(e,t,i)=>{i.r(t);i.d(t,{ARIAGlobalStatesAndProperties:()=>$i,Accordion:()=>xi,AccordionExpandMode:()=>Ci,AccordionItem:()=>He,Anchor:()=>ki,AnchoredRegion:()=>ro,Avatar:()=>vo,Badge:()=>go,BaseProgress:()=>_l,Breadcrumb:()=>wo,BreadcrumbItem:()=>Co,Button:()=>Ao,Calendar:()=>Po,CalendarTitleTemplate:()=>jo,Card:()=>Zo,CheckableFormAssociated:()=>Ro,Checkbox:()=>ir,Combobox:()=>Ar,ComboboxAutocomplete:()=>Dr,ComponentPresentation:()=>De,Container:()=>q,ContainerConfiguration:()=>z,ContainerImpl:()=>ge,DI:()=>U,DataGrid:()=>qo,DataGridCell:()=>Bo,DataGridCellTypes:()=>Ho,DataGridRow:()=>Uo,DataGridRowTypes:()=>zo,DateFormatter:()=>Lo,DefaultComponentPresentation:()=>Ae,DefaultResolver:()=>H,DelegatesARIAButton:()=>Fo,DelegatesARIACombobox:()=>Fr,DelegatesARIALink:()=>Ii,DelegatesARIAListbox:()=>Or,DelegatesARIAListboxOption:()=>Ir,DelegatesARIASearch:()=>rd,DelegatesARIASelect:()=>hd,DelegatesARIATextbox:()=>Vl,DelegatesARIAToolbar:()=>qd,DesignSystem:()=>ma,DesignToken:()=>da,Dialog:()=>Ga,Disclosure:()=>el,Divider:()=>nl,DividerRole:()=>sl,ElementDisambiguation:()=>ha,FactoryImpl:()=>de,Flipper:()=>al,FlipperDirection:()=>ol,FlyoutPosBottom:()=>ho,FlyoutPosBottomFill:()=>po,FlyoutPosTallest:()=>co,FlyoutPosTallestFill:()=>fo,FlyoutPosTop:()=>lo,FlyoutPosTopFill:()=>uo,FormAssociated:()=>To,FoundationElement:()=>Fe,FoundationElementRegistry:()=>Pe,GenerateHeaderOptions:()=>Mo,HorizontalScroll:()=>Jl,Listbox:()=>Er,ListboxElement:()=>dl,ListboxOption:()=>kr,MatchMediaBehavior:()=>Zd,MatchMediaStyleSheetBehavior:()=>Jd,Menu:()=>Fl,MenuItem:()=>Dl,MenuItemRole:()=>Tl,NumberField:()=>Ul,Picker:()=>$l,PickerList:()=>fl,PickerListItem:()=>vl,PickerMenu:()=>cl,PickerMenuOption:()=>pl,PropertyStyleSheetBehavior:()=>sh,Radio:()=>Zl,RadioGroup:()=>Gl,Registration:()=>xe,ResolverBuilder:()=>P,ResolverImpl:()=>re,Search:()=>od,Select:()=>dd,SelectPosition:()=>Tr,ServiceLocator:()=>j,Skeleton:()=>pd,Slider:()=>wd,SliderLabel:()=>bd,SliderMode:()=>xd,StartEnd:()=>n,Switch:()=>Ed,Tab:()=>Sd,TabPanel:()=>Td,Tabs:()=>Fd,TabsOrientation:()=>Ad,TextArea:()=>zd,TextAreaResize:()=>Ld,TextField:()=>zl,TextFieldType:()=>Hl,Toolbar:()=>Ud,Tooltip:()=>Kd,TooltipPosition:()=>_d,TreeItem:()=>Yd,TreeView:()=>Qd,accordionItemTemplate:()=>d,accordionTemplate:()=>ze,all:()=>J,anchorTemplate:()=>wi,anchoredRegionTemplate:()=>Ei,applyMixins:()=>Me,avatarTemplate:()=>mo,badgeTemplate:()=>bo,breadcrumbItemTemplate:()=>yo,breadcrumbTemplate:()=>xo,buttonTemplate:()=>$o,calendarCellTemplate:()=>Ko,calendarRowTemplate:()=>Wo,calendarTemplate:()=>Xo,calendarWeekdayTemplate:()=>_o,cardTemplate:()=>Qo,checkboxTemplate:()=>Jo,comboboxTemplate:()=>Lr,composedContains:()=>Ur,composedParent:()=>Br,darkModeStylesheetBehavior:()=>th,dataGridCellTemplate:()=>Nr,dataGridRowTemplate:()=>Vr,dataGridTemplate:()=>Mr,dialogTemplate:()=>ya,disabledCursor:()=>nh,disclosureTemplate:()=>Ja,display:()=>rh,dividerTemplate:()=>tl,endSlotTemplate:()=>o,endTemplate:()=>a,flipperTemplate:()=>rl,focusVisible:()=>ah,forcedColorsStylesheetBehavior:()=>eh,getDirection:()=>no,hidden:()=>oh,horizontalScrollTemplate:()=>ed,ignore:()=>ie,inject:()=>K,interactiveCalendarGridTemplate:()=>Go,isListboxOption:()=>$r,isTreeItemElement:()=>Gd,lazy:()=>ee,lightModeStylesheetBehavior:()=>ih,listboxOptionTemplate:()=>ll,listboxTemplate:()=>hl,menuItemTemplate:()=>Sl,menuTemplate:()=>Al,newInstanceForScope:()=>se,newInstanceOf:()=>ne,noninteractiveCalendarTemplate:()=>Yo,numberFieldTemplate:()=>Ll,optional:()=>te,pickerListItemTemplate:()=>Ol,pickerListTemplate:()=>El,pickerMenuOptionTemplate:()=>Il,pickerMenuTemplate:()=>kl,pickerTemplate:()=>yl,progressRingTemplate:()=>jl,progressTemplate:()=>Kl,radioGroupTemplate:()=>Wl,radioTemplate:()=>Yl,reflectAttributes:()=>Za,roleForMenuItem:()=>Rl,searchTemplate:()=>id,selectTemplate:()=>cd,singleton:()=>Q,skeletonTemplate:()=>ud,sliderLabelTemplate:()=>fd,sliderTemplate:()=>gd,startSlotTemplate:()=>r,startTemplate:()=>l,supportsElementInternals:()=>Eo,switchTemplate:()=>$d,tabPanelTemplate:()=>Od,tabTemplate:()=>Rd,tabsTemplate:()=>Dd,textAreaTemplate:()=>Pd,textFieldTemplate:()=>Vd,toolbarTemplate:()=>Nd,tooltipTemplate:()=>jd,transient:()=>G,treeItemTemplate:()=>Wd,treeViewTemplate:()=>Xd,validateKey:()=>we,whitespaceFilter:()=>td});var s=i(81351);class n{handleStartContentChange(){this.startContainer.classList.toggle("start",this.start.assignedNodes().length>0)}handleEndContentChange(){this.endContainer.classList.toggle("end",this.end.assignedNodes().length>0)}}const o=(e,t)=>s.html`
    <span
        part="end"
        ${(0,s.ref)("endContainer")}
        class=${e=>t.end?"end":void 0}
    >
        <slot name="end" ${(0,s.ref)("end")} @slotchange="${e=>e.handleEndContentChange()}">
            ${t.end||""}
        </slot>
    </span>
`;const r=(e,t)=>s.html`
    <span
        part="start"
        ${(0,s.ref)("startContainer")}
        class="${e=>t.start?"start":void 0}"
    >
        <slot
            name="start"
            ${(0,s.ref)("start")}
            @slotchange="${e=>e.handleStartContentChange()}"
        >
            ${t.start||""}
        </slot>
    </span>
`;const a=s.html`
    <span part="end" ${(0,s.ref)("endContainer")}>
        <slot
            name="end"
            ${(0,s.ref)("end")}
            @slotchange="${e=>e.handleEndContentChange()}"
        ></slot>
    </span>
`;const l=s.html`
    <span part="start" ${(0,s.ref)("startContainer")}>
        <slot
            name="start"
            ${(0,s.ref)("start")}
            @slotchange="${e=>e.handleStartContentChange()}"
        ></slot>
    </span>
`;const d=(e,t)=>s.html`
    <template class="${e=>e.expanded?"expanded":""}">
        <div
            class="heading"
            part="heading"
            role="heading"
            aria-level="${e=>e.headinglevel}"
        >
            <button
                class="button"
                part="button"
                ${(0,s.ref)("expandbutton")}
                aria-expanded="${e=>e.expanded}"
                aria-controls="${e=>e.id}-panel"
                id="${e=>e.id}"
                @click="${(e,t)=>e.clickHandler(t.event)}"
            >
                <span class="heading-content" part="heading-content">
                    <slot name="heading"></slot>
                </span>
            </button>
            ${r(e,t)}
            ${o(e,t)}
            <span class="icon" part="icon" aria-hidden="true">
                <slot name="expanded-icon" part="expanded-icon">
                    ${t.expandedIcon||""}
                </slot>
                <slot name="collapsed-icon" part="collapsed-icon">
                    ${t.collapsedIcon||""}
                </slot>
            <span>
        </div>
        <div
            class="region"
            part="region"
            id="${e=>e.id}-panel"
            role="region"
            aria-labelledby="${e=>e.id}"
        >
            <slot></slot>
        </div>
    </template>
`;var h=function(e,t){h=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(e,t){e.__proto__=t}||function(e,t){for(var i in t)if(t.hasOwnProperty(i))e[i]=t[i]};return h(e,t)};function c(e,t){h(e,t);function i(){this.constructor=e}e.prototype=t===null?Object.create(t):(i.prototype=t.prototype,new i)}var u=function(){u=Object.assign||function e(t){for(var i,s=1,n=arguments.length;s<n;s++){i=arguments[s];for(var o in i)if(Object.prototype.hasOwnProperty.call(i,o))t[o]=i[o]}return t};return u.apply(this,arguments)};function p(e,t){var i={};for(var s in e)if(Object.prototype.hasOwnProperty.call(e,s)&&t.indexOf(s)<0)i[s]=e[s];if(e!=null&&typeof Object.getOwnPropertySymbols==="function")for(var n=0,s=Object.getOwnPropertySymbols(e);n<s.length;n++){if(t.indexOf(s[n])<0&&Object.prototype.propertyIsEnumerable.call(e,s[n]))i[s[n]]=e[s[n]]}return i}function f(e,t,i,s){var n=arguments.length,o=n<3?t:s===null?s=Object.getOwnPropertyDescriptor(t,i):s,r;if(typeof Reflect==="object"&&typeof Reflect.decorate==="function")o=Reflect.decorate(e,t,i,s);else for(var a=e.length-1;a>=0;a--)if(r=e[a])o=(n<3?r(o):n>3?r(t,i,o):r(t,i))||o;return n>3&&o&&Object.defineProperty(t,i,o),o}function m(e,t){return function(i,s){t(i,s,e)}}function v(e,t){if(typeof Reflect==="object"&&typeof Reflect.metadata==="function")return Reflect.metadata(e,t)}function b(e,t,i,s){function n(e){return e instanceof i?e:new i((function(t){t(e)}))}return new(i||(i=Promise))((function(i,o){function r(e){try{l(s.next(e))}catch(t){o(t)}}function a(e){try{l(s["throw"](e))}catch(t){o(t)}}function l(e){e.done?i(e.value):n(e.value).then(r,a)}l((s=s.apply(e,t||[])).next())}))}function g(e,t){var i={label:0,sent:function(){if(o[0]&1)throw o[1];return o[1]},trys:[],ops:[]},s,n,o,r;return r={next:a(0),throw:a(1),return:a(2)},typeof Symbol==="function"&&(r[Symbol.iterator]=function(){return this}),r;function a(e){return function(t){return l([e,t])}}function l(r){if(s)throw new TypeError("Generator is already executing.");while(i)try{if(s=1,n&&(o=r[0]&2?n["return"]:r[0]?n["throw"]||((o=n["return"])&&o.call(n),0):n.next)&&!(o=o.call(n,r[1])).done)return o;if(n=0,o)r=[r[0]&2,o.value];switch(r[0]){case 0:case 1:o=r;break;case 4:i.label++;return{value:r[1],done:false};case 5:i.label++;n=r[1];r=[0];continue;case 7:r=i.ops.pop();i.trys.pop();continue;default:if(!(o=i.trys,o=o.length>0&&o[o.length-1])&&(r[0]===6||r[0]===2)){i=0;continue}if(r[0]===3&&(!o||r[1]>o[0]&&r[1]<o[3])){i.label=r[1];break}if(r[0]===6&&i.label<o[1]){i.label=o[1];o=r;break}if(o&&i.label<o[2]){i.label=o[2];i.ops.push(r);break}if(o[2])i.ops.pop();i.trys.pop();continue}r=t.call(e,i)}catch(a){r=[6,a];n=0}finally{s=o=0}if(r[0]&5)throw r[1];return{value:r[0]?r[1]:void 0,done:true}}}function y(e,t,i,s){if(s===undefined)s=i;e[s]=t[i]}function C(e,t){for(var i in e)if(i!=="default"&&!t.hasOwnProperty(i))t[i]=e[i]}function x(e){var t=typeof Symbol==="function"&&Symbol.iterator,i=t&&e[t],s=0;if(i)return i.call(e);if(e&&typeof e.length==="number")return{next:function(){if(e&&s>=e.length)e=void 0;return{value:e&&e[s++],done:!e}}};throw new TypeError(t?"Object is not iterable.":"Symbol.iterator is not defined.")}function w(e,t){var i=typeof Symbol==="function"&&e[Symbol.iterator];if(!i)return e;var s=i.call(e),n,o=[],r;try{while((t===void 0||t-- >0)&&!(n=s.next()).done)o.push(n.value)}catch(a){r={error:a}}finally{try{if(n&&!n.done&&(i=s["return"]))i.call(s)}finally{if(r)throw r.error}}return o}function $(){for(var e=[],t=0;t<arguments.length;t++)e=e.concat(w(arguments[t]));return e}function k(){for(var e=0,t=0,i=arguments.length;t<i;t++)e+=arguments[t].length;for(var s=Array(e),n=0,t=0;t<i;t++)for(var o=arguments[t],r=0,a=o.length;r<a;r++,n++)s[n]=o[r];return s}function I(e){return this instanceof I?(this.v=e,this):new I(e)}function E(e,t,i){if(!Symbol.asyncIterator)throw new TypeError("Symbol.asyncIterator is not defined.");var s=i.apply(e,t||[]),n,o=[];return n={},r("next"),r("throw"),r("return"),n[Symbol.asyncIterator]=function(){return this},n;function r(e){if(s[e])n[e]=function(t){return new Promise((function(i,s){o.push([e,t,i,s])>1||a(e,t)}))}}function a(e,t){try{l(s[e](t))}catch(i){c(o[0][3],i)}}function l(e){e.value instanceof I?Promise.resolve(e.value.v).then(d,h):c(o[0][2],e)}function d(e){a("next",e)}function h(e){a("throw",e)}function c(e,t){if(e(t),o.shift(),o.length)a(o[0][0],o[0][1])}}function O(e){var t,i;return t={},s("next"),s("throw",(function(e){throw e})),s("return"),t[Symbol.iterator]=function(){return this},t;function s(s,n){t[s]=e[s]?function(t){return(i=!i)?{value:I(e[s](t)),done:s==="return"}:n?n(t):t}:n}}function T(e){if(!Symbol.asyncIterator)throw new TypeError("Symbol.asyncIterator is not defined.");var t=e[Symbol.asyncIterator],i;return t?t.call(e):(e=typeof x==="function"?x(e):e[Symbol.iterator](),i={},s("next"),s("throw"),s("return"),i[Symbol.asyncIterator]=function(){return this},i);function s(t){i[t]=e[t]&&function(i){return new Promise((function(s,o){i=e[t](i),n(s,o,i.done,i.value)}))}}function n(e,t,i,s){Promise.resolve(s).then((function(t){e({value:t,done:i})}),t)}}function R(e,t){if(Object.defineProperty){Object.defineProperty(e,"raw",{value:t})}else{e.raw=t}return e}function S(e){if(e&&e.__esModule)return e;var t={};if(e!=null)for(var i in e)if(Object.hasOwnProperty.call(e,i))t[i]=e[i];t.default=e;return t}function D(e){return e&&e.__esModule?e:{default:e}}function A(e,t){if(!t.has(e)){throw new TypeError("attempted to get private field on non-instance")}return t.get(e)}function F(e,t,i){if(!t.has(e)){throw new TypeError("attempted to set private field on non-instance")}t.set(e,i);return i}const L=new Map;if(!("metadata"in Reflect)){Reflect.metadata=function(e,t){return function(i){Reflect.defineMetadata(e,t,i)}};Reflect.defineMetadata=function(e,t,i){let s=L.get(i);if(s===void 0){L.set(i,s=new Map)}s.set(e,t)};Reflect.getOwnMetadata=function(e,t){const i=L.get(t);if(i!==void 0){return i.get(e)}return void 0}}class P{constructor(e,t){this.container=e;this.key=t}instance(e){return this.registerResolver(0,e)}singleton(e){return this.registerResolver(1,e)}transient(e){return this.registerResolver(2,e)}callback(e){return this.registerResolver(3,e)}cachedCallback(e){return this.registerResolver(3,Ce(e))}aliasTo(e){return this.registerResolver(5,e)}registerResolver(e,t){const{container:i,key:s}=this;this.container=this.key=void 0;return i.registerResolver(s,new re(s,e,t))}}function M(e){const t=e.slice();const i=Object.keys(e);const s=i.length;let n;for(let o=0;o<s;++o){n=i[o];if(!Te(n)){t[n]=e[n]}}return t}const H=Object.freeze({none(e){throw Error(`${e.toString()} not registered, did you forget to add @singleton()?`)},singleton(e){return new re(e,1,e)},transient(e){return new re(e,2,e)}});const z=Object.freeze({default:Object.freeze({parentLocator:()=>null,responsibleForOwnerRequests:false,defaultResolver:H.singleton})});const V=new Map;function N(e){return t=>Reflect.getOwnMetadata(e,t)}let B=null;const U=Object.freeze({createContainer(e){return new ge(null,Object.assign({},z.default,e))},findResponsibleContainer(e){const t=e.$$container$$;if(t&&t.responsibleForOwnerRequests){return t}return U.findParentContainer(e)},findParentContainer(e){const t=new CustomEvent(ve,{bubbles:true,composed:true,cancelable:true,detail:{container:void 0}});e.dispatchEvent(t);return t.detail.container||U.getOrCreateDOMContainer()},getOrCreateDOMContainer(e,t){if(!e){return B||(B=new ge(null,Object.assign({},z.default,t,{parentLocator:()=>null})))}return e.$$container$$||new ge(e,Object.assign({},z.default,t,{parentLocator:U.findParentContainer}))},getDesignParamtypes:N("design:paramtypes"),getAnnotationParamtypes:N("di:paramtypes"),getOrCreateAnnotationParamTypes(e){let t=this.getAnnotationParamtypes(e);if(t===void 0){Reflect.defineMetadata("di:paramtypes",t=[],e)}return t},getDependencies(e){let t=V.get(e);if(t===void 0){const i=e.inject;if(i===void 0){const i=U.getDesignParamtypes(e);const s=U.getAnnotationParamtypes(e);if(i===void 0){if(s===void 0){const i=Object.getPrototypeOf(e);if(typeof i==="function"&&i!==Function.prototype){t=M(U.getDependencies(i))}else{t=[]}}else{t=M(s)}}else if(s===void 0){t=M(i)}else{t=M(i);let e=s.length;let n;for(let i=0;i<e;++i){n=s[i];if(n!==void 0){t[i]=n}}const o=Object.keys(s);e=o.length;let r;for(let i=0;i<e;++i){r=o[i];if(!Te(r)){t[r]=s[r]}}}}else{t=M(i)}V.set(e,t)}return t},defineProperty(e,t,i,n=false){const o=`$di_${t}`;Reflect.defineProperty(e,t,{get:function(){let e=this[o];if(e===void 0){const r=this instanceof HTMLElement?U.findResponsibleContainer(this):U.getOrCreateDOMContainer();e=r.get(i);this[o]=e;if(n&&this instanceof s.FASTElement){const s=this.$fastController;const n=()=>{const n=U.findResponsibleContainer(this);const r=n.get(i);const a=this[o];if(r!==a){this[o]=e;s.notify(t)}};s.subscribe({handleChange:n},"isConnected")}}return e}})},createInterface(e,t){const i=typeof e==="function"?e:t;const s=typeof e==="string"?e:e&&"friendlyName"in e?e.friendlyName||ke:ke;const n=typeof e==="string"?false:e&&"respectConnection"in e?e.respectConnection||false:false;const o=function(e,t,i){if(e==null||new.target!==undefined){throw new Error(`No registration for interface: '${o.friendlyName}'`)}if(t){U.defineProperty(e,t,o,n)}else{const t=U.getOrCreateAnnotationParamTypes(e);t[i]=o}};o.$isInterface=true;o.friendlyName=s==null?"(anonymous)":s;if(i!=null){o.register=function(e,t){return i(new P(e,t!==null&&t!==void 0?t:o))}}o.toString=function e(){return`InterfaceSymbol<${o.friendlyName}>`};return o},inject(...e){return function(t,i,s){if(typeof s==="number"){const i=U.getOrCreateAnnotationParamTypes(t);const n=e[0];if(n!==void 0){i[s]=n}}else if(i){U.defineProperty(t,i,e[0])}else{const i=s?U.getOrCreateAnnotationParamTypes(s.value):U.getOrCreateAnnotationParamTypes(t);let n;for(let t=0;t<e.length;++t){n=e[t];if(n!==void 0){i[t]=n}}}}},transient(e){e.register=function t(i){const s=xe.transient(e,e);return s.register(i)};e.registerInRequestor=false;return e},singleton(e,t=Y){e.register=function t(i){const s=xe.singleton(e,e);return s.register(i)};e.registerInRequestor=t.scoped;return e}});const q=U.createInterface("Container");const j=q;function _(e){return function(t){const i=function(e,t,s){U.inject(i)(e,t,s)};i.$isResolver=true;i.resolve=function(i,s){return e(t,i,s)};return i}}const K=U.inject;function W(e){return U.transient(e)}function G(e){return e==null?W:W(e)}const Y={scoped:false};function X(e){return U.singleton(e)}function Q(e){if(typeof e==="function"){return U.singleton(e)}return function(t){return U.singleton(t,e)}}function Z(e){return function(t,i){i=!!i;const s=function(e,t,i){U.inject(s)(e,t,i)};s.$isResolver=true;s.resolve=function(s,n){return e(t,s,n,i)};return s}}const J=Z(((e,t,i,s)=>i.getAll(e,s)));const ee=_(((e,t,i)=>()=>i.get(e)));const te=_(((e,t,i)=>{if(i.has(e,true)){return i.get(e)}else{return undefined}}));function ie(e,t,i){U.inject(ie)(e,t,i)}ie.$isResolver=true;ie.resolve=()=>undefined;const se=_(((e,t,i)=>{const s=oe(e,t);const n=new re(e,0,s);i.registerResolver(e,n);return s}));const ne=_(((e,t,i)=>oe(e,t)));function oe(e,t){return t.getFactory(e).construct(t)}class re{constructor(e,t,i){this.key=e;this.strategy=t;this.state=i;this.resolving=false}get $isResolver(){return true}register(e){return e.registerResolver(this.key,this)}resolve(e,t){switch(this.strategy){case 0:return this.state;case 1:{if(this.resolving){throw new Error(`Cyclic dependency found: ${this.state.name}`)}this.resolving=true;this.state=e.getFactory(this.state).construct(t);this.strategy=0;this.resolving=false;return this.state}case 2:{const i=e.getFactory(this.state);if(i===null){throw new Error(`Resolver for ${String(this.key)} returned a null factory`)}return i.construct(t)}case 3:return this.state(e,t,this);case 4:return this.state[0].resolve(e,t);case 5:return t.get(this.state);default:throw new Error(`Invalid resolver strategy specified: ${this.strategy}.`)}}getFactory(e){var t,i,s;switch(this.strategy){case 1:case 2:return e.getFactory(this.state);case 5:return(s=(i=(t=e.getResolver(this.state))===null||t===void 0?void 0:t.getFactory)===null||i===void 0?void 0:i.call(t,e))!==null&&s!==void 0?s:null;default:return null}}}function ae(e){return this.get(e)}function le(e,t){return t(e)}class de{constructor(e,t){this.Type=e;this.dependencies=t;this.transformers=null}construct(e,t){let i;if(t===void 0){i=new this.Type(...this.dependencies.map(ae,e))}else{i=new this.Type(...this.dependencies.map(ae,e),...t)}if(this.transformers==null){return i}return this.transformers.reduce(le,i)}registerTransformer(e){(this.transformers||(this.transformers=[])).push(e)}}const he={$isResolver:true,resolve(e,t){return t}};function ce(e){return typeof e.register==="function"}function ue(e){return ce(e)&&typeof e.registerInRequestor==="boolean"}function pe(e){return ue(e)&&e.registerInRequestor}function fe(e){return e.prototype!==void 0}const me=new Set(["Array","ArrayBuffer","Boolean","DataView","Date","Error","EvalError","Float32Array","Float64Array","Function","Int8Array","Int16Array","Int32Array","Map","Number","Object","Promise","RangeError","ReferenceError","RegExp","Set","SharedArrayBuffer","String","SyntaxError","TypeError","Uint8Array","Uint8ClampedArray","Uint16Array","Uint32Array","URIError","WeakMap","WeakSet"]);const ve="__DI_LOCATE_PARENT__";const be=new Map;class ge{constructor(e,t){this.owner=e;this.config=t;this._parent=void 0;this.registerDepth=0;this.context=null;if(e!==null){e.$$container$$=this}this.resolvers=new Map;this.resolvers.set(q,he);if(e instanceof Node){e.addEventListener(ve,(e=>{if(e.composedPath()[0]!==this.owner){e.detail.container=this;e.stopImmediatePropagation()}}))}}get parent(){if(this._parent===void 0){this._parent=this.config.parentLocator(this.owner)}return this._parent}get depth(){return this.parent===null?0:this.parent.depth+1}get responsibleForOwnerRequests(){return this.config.responsibleForOwnerRequests}registerWithContext(e,...t){this.context=e;this.register(...t);this.context=null;return this}register(...e){if(++this.registerDepth===100){throw new Error("Unable to autoregister dependency")}let t;let i;let s;let n;let o;const r=this.context;for(let a=0,l=e.length;a<l;++a){t=e[a];if(!Ie(t)){continue}if(ce(t)){t.register(this,r)}else if(fe(t)){xe.singleton(t,t).register(this)}else{i=Object.keys(t);n=0;o=i.length;for(;n<o;++n){s=t[i[n]];if(!Ie(s)){continue}if(ce(s)){s.register(this,r)}else{this.register(s)}}}}--this.registerDepth;return this}registerResolver(e,t){we(e);const i=this.resolvers;const s=i.get(e);if(s==null){i.set(e,t)}else if(s instanceof re&&s.strategy===4){s.state.push(t)}else{i.set(e,new re(e,4,[s,t]))}return t}registerTransformer(e,t){const i=this.getResolver(e);if(i==null){return false}if(i.getFactory){const e=i.getFactory(this);if(e==null){return false}e.registerTransformer(t);return true}return false}getResolver(e,t=true){we(e);if(e.resolve!==void 0){return e}let i=this;let s;while(i!=null){s=i.resolvers.get(e);if(s==null){if(i.parent==null){const s=pe(e)?this:i;return t?this.jitRegister(e,s):null}i=i.parent}else{return s}}return null}has(e,t=false){return this.resolvers.has(e)?true:t&&this.parent!=null?this.parent.has(e,true):false}get(e){we(e);if(e.$isResolver){return e.resolve(this,this)}let t=this;let i;while(t!=null){i=t.resolvers.get(e);if(i==null){if(t.parent==null){const s=pe(e)?this:t;i=this.jitRegister(e,s);return i.resolve(t,this)}t=t.parent}else{return i.resolve(t,this)}}throw new Error(`Unable to resolve key: ${String(e)}`)}getAll(e,t=false){we(e);const i=this;let n=i;let o;if(t){let t=s.emptyArray;while(n!=null){o=n.resolvers.get(e);if(o!=null){t=t.concat($e(o,n,i))}n=n.parent}return t}else{while(n!=null){o=n.resolvers.get(e);if(o==null){n=n.parent;if(n==null){return s.emptyArray}}else{return $e(o,n,i)}}}return s.emptyArray}getFactory(e){let t=be.get(e);if(t===void 0){if(Ee(e)){throw new Error(`${e.name} is a native function and therefore cannot be safely constructed by DI. If this is intentional, please use a callback or cachedCallback resolver.`)}be.set(e,t=new de(e,U.getDependencies(e)))}return t}registerFactory(e,t){be.set(e,t)}createChild(e){return new ge(null,Object.assign({},this.config,e,{parentLocator:()=>this}))}jitRegister(e,t){if(typeof e!=="function"){throw new Error(`Attempted to jitRegister something that is not a constructor: '${e}'. Did you forget to register this dependency?`)}if(me.has(e.name)){throw new Error(`Attempted to jitRegister an intrinsic type: ${e.name}. Did you forget to add @inject(Key)`)}if(ce(e)){const i=e.register(t);if(!(i instanceof Object)||i.resolve==null){const i=t.resolvers.get(e);if(i!=void 0){return i}throw new Error("A valid resolver was not returned from the static register method")}return i}else if(e.$isInterface){throw new Error(`Attempted to jitRegister an interface: ${e.friendlyName}`)}else{const i=this.config.defaultResolver(e,t);t.resolvers.set(e,i);return i}}}const ye=new WeakMap;function Ce(e){return function(t,i,s){if(ye.has(s)){return ye.get(s)}const n=e(t,i,s);ye.set(s,n);return n}}const xe=Object.freeze({instance(e,t){return new re(e,0,t)},singleton(e,t){return new re(e,1,t)},transient(e,t){return new re(e,2,t)},callback(e,t){return new re(e,3,t)},cachedCallback(e,t){return new re(e,3,Ce(t))},aliasTo(e,t){return new re(t,5,e)}});function we(e){if(e===null||e===void 0){throw new Error("key/value cannot be null or undefined. Are you trying to inject/register something that doesn't exist with DI?")}}function $e(e,t,i){if(e instanceof re&&e.strategy===4){const s=e.state;let n=s.length;const o=new Array(n);while(n--){o[n]=s[n].resolve(t,i)}return o}return[e.resolve(t,i)]}const ke="(anonymous)";function Ie(e){return typeof e==="object"&&e!==null||typeof e==="function"}const Ee=function(){const e=new WeakMap;let t=false;let i="";let s=0;return function(n){t=e.get(n);if(t===void 0){i=n.toString();s=i.length;t=s>=29&&s<=100&&i.charCodeAt(s-1)===125&&i.charCodeAt(s-2)<=32&&i.charCodeAt(s-3)===93&&i.charCodeAt(s-4)===101&&i.charCodeAt(s-5)===100&&i.charCodeAt(s-6)===111&&i.charCodeAt(s-7)===99&&i.charCodeAt(s-8)===32&&i.charCodeAt(s-9)===101&&i.charCodeAt(s-10)===118&&i.charCodeAt(s-11)===105&&i.charCodeAt(s-12)===116&&i.charCodeAt(s-13)===97&&i.charCodeAt(s-14)===110&&i.charCodeAt(s-15)===88;e.set(n,t)}return t}}();const Oe={};function Te(e){switch(typeof e){case"number":return e>=0&&(e|0)===e;case"string":{const t=Oe[e];if(t!==void 0){return t}const i=e.length;if(i===0){return Oe[e]=false}let s=0;for(let n=0;n<i;++n){s=e.charCodeAt(n);if(n===0&&s===48&&i>1||s<48||s>57){return Oe[e]=false}}return Oe[e]=true}default:return false}}function Re(e){return`${e.toLowerCase()}:presentation`}const Se=new Map;const De=Object.freeze({define(e,t,i){const s=Re(e);const n=Se.get(s);if(n===void 0){Se.set(s,t)}else{Se.set(s,false)}i.register(xe.instance(s,t))},forTag(e,t){const i=Re(e);const s=Se.get(i);if(s===false){const e=U.findResponsibleContainer(t);return e.get(i)}return s||null}});class Ae{constructor(e,t){this.template=e||null;this.styles=t===void 0?null:Array.isArray(t)?s.ElementStyles.create(t):t instanceof s.ElementStyles?t:s.ElementStyles.create([t])}applyTo(e){const t=e.$fastController;if(t.template===null){t.template=this.template}if(t.styles===null){t.styles=this.styles}}}class Fe extends s.FASTElement{constructor(){super(...arguments);this._presentation=void 0}get $presentation(){if(this._presentation===void 0){this._presentation=De.forTag(this.tagName,this)}return this._presentation}templateChanged(){if(this.template!==undefined){this.$fastController.template=this.template}}stylesChanged(){if(this.styles!==undefined){this.$fastController.styles=this.styles}}connectedCallback(){if(this.$presentation!==null){this.$presentation.applyTo(this)}super.connectedCallback()}static compose(e){return(t={})=>new Pe(this===Fe?class extends Fe{}:this,e,t)}}f([s.observable],Fe.prototype,"template",void 0);f([s.observable],Fe.prototype,"styles",void 0);function Le(e,t,i){if(typeof e==="function"){return e(t,i)}return e}class Pe{constructor(e,t,i){this.type=e;this.elementDefinition=t;this.overrideDefinition=i;this.definition=Object.assign(Object.assign({},this.elementDefinition),this.overrideDefinition)}register(e,t){const i=this.definition;const s=this.overrideDefinition;const n=i.prefix||t.elementPrefix;const o=`${n}-${i.baseName}`;t.tryDefineElement({name:o,type:this.type,baseClass:this.elementDefinition.baseClass,callback:e=>{const t=new Ae(Le(i.template,e,i),Le(i.styles,e,i));e.definePresentation(t);let n=Le(i.shadowOptions,e,i);if(e.shadowRootMode){if(n){if(!s.shadowOptions){n.mode=e.shadowRootMode}}else if(n!==null){n={mode:e.shadowRootMode}}}e.defineElement({elementOptions:Le(i.elementOptions,e,i),shadowOptions:n,attributes:Le(i.attributes,e,i)})}})}}function Me(e,...t){const i=s.AttributeConfiguration.locate(e);t.forEach((t=>{Object.getOwnPropertyNames(t.prototype).forEach((i=>{if(i!=="constructor"){Object.defineProperty(e.prototype,i,Object.getOwnPropertyDescriptor(t.prototype,i))}}));const n=s.AttributeConfiguration.locate(t);n.forEach((e=>i.push(e)))}))}class He extends Fe{constructor(){super(...arguments);this.headinglevel=2;this.expanded=false;this.clickHandler=e=>{this.expanded=!this.expanded;this.change()};this.change=()=>{this.$emit("change")}}}f([(0,s.attr)({attribute:"heading-level",mode:"fromView",converter:s.nullableNumberConverter})],He.prototype,"headinglevel",void 0);f([(0,s.attr)({mode:"boolean"})],He.prototype,"expanded",void 0);f([s.attr],He.prototype,"id",void 0);Me(He,n);const ze=(e,t)=>s.html`
    <template>
        <slot ${(0,s.slotted)({property:"accordionItems",filter:(0,s.elements)()})}></slot>
        <slot name="item" part="item" ${(0,s.slotted)("accordionItems")}></slot>
    </template>
`;var Ve;(function(e){e[e["alt"]=18]="alt";e[e["arrowDown"]=40]="arrowDown";e[e["arrowLeft"]=37]="arrowLeft";e[e["arrowRight"]=39]="arrowRight";e[e["arrowUp"]=38]="arrowUp";e[e["back"]=8]="back";e[e["backSlash"]=220]="backSlash";e[e["break"]=19]="break";e[e["capsLock"]=20]="capsLock";e[e["closeBracket"]=221]="closeBracket";e[e["colon"]=186]="colon";e[e["colon2"]=59]="colon2";e[e["comma"]=188]="comma";e[e["ctrl"]=17]="ctrl";e[e["delete"]=46]="delete";e[e["end"]=35]="end";e[e["enter"]=13]="enter";e[e["equals"]=187]="equals";e[e["equals2"]=61]="equals2";e[e["equals3"]=107]="equals3";e[e["escape"]=27]="escape";e[e["forwardSlash"]=191]="forwardSlash";e[e["function1"]=112]="function1";e[e["function10"]=121]="function10";e[e["function11"]=122]="function11";e[e["function12"]=123]="function12";e[e["function2"]=113]="function2";e[e["function3"]=114]="function3";e[e["function4"]=115]="function4";e[e["function5"]=116]="function5";e[e["function6"]=117]="function6";e[e["function7"]=118]="function7";e[e["function8"]=119]="function8";e[e["function9"]=120]="function9";e[e["home"]=36]="home";e[e["insert"]=45]="insert";e[e["menu"]=93]="menu";e[e["minus"]=189]="minus";e[e["minus2"]=109]="minus2";e[e["numLock"]=144]="numLock";e[e["numPad0"]=96]="numPad0";e[e["numPad1"]=97]="numPad1";e[e["numPad2"]=98]="numPad2";e[e["numPad3"]=99]="numPad3";e[e["numPad4"]=100]="numPad4";e[e["numPad5"]=101]="numPad5";e[e["numPad6"]=102]="numPad6";e[e["numPad7"]=103]="numPad7";e[e["numPad8"]=104]="numPad8";e[e["numPad9"]=105]="numPad9";e[e["numPadDivide"]=111]="numPadDivide";e[e["numPadDot"]=110]="numPadDot";e[e["numPadMinus"]=109]="numPadMinus";e[e["numPadMultiply"]=106]="numPadMultiply";e[e["numPadPlus"]=107]="numPadPlus";e[e["openBracket"]=219]="openBracket";e[e["pageDown"]=34]="pageDown";e[e["pageUp"]=33]="pageUp";e[e["period"]=190]="period";e[e["print"]=44]="print";e[e["quote"]=222]="quote";e[e["scrollLock"]=145]="scrollLock";e[e["shift"]=16]="shift";e[e["space"]=32]="space";e[e["tab"]=9]="tab";e[e["tilde"]=192]="tilde";e[e["windowsLeft"]=91]="windowsLeft";e[e["windowsOpera"]=219]="windowsOpera";e[e["windowsRight"]=92]="windowsRight"})(Ve||(Ve={}));const Ne=18;const Be=40;const Ue=37;const qe=39;const je=38;const _e=8;const Ke=220;const We=19;const Ge=20;const Ye=221;const Xe=186;const Qe=59;const Ze=188;const Je=17;const et=46;const tt=35;const it=13;const st=187;const nt=61;const ot=107;const rt=27;const at=191;const lt=112;const dt=121;const ht=122;const ct=123;const ut=113;const pt=114;const ft=115;const mt=116;const vt=117;const bt=118;const gt=119;const yt=120;const Ct=36;const xt=45;const wt=93;const $t=189;const kt=109;const It=144;const Et=96;const Ot=97;const Tt=98;const Rt=99;const St=100;const Dt=101;const At=102;const Ft=103;const Lt=104;const Pt=105;const Mt=111;const Ht=110;const zt=109;const Vt=106;const Nt=107;const Bt=219;const Ut=34;const qt=33;const jt=190;const _t=44;const Kt=222;const Wt=145;const Gt=16;const Yt=32;const Xt=9;const Qt=192;const Zt=91;const Jt=219;const ei=92;const ti="ArrowDown";const ii="ArrowLeft";const si="ArrowRight";const ni="ArrowUp";const oi="Enter";const ri="Escape";const ai="Home";const li="End";const di="F2";const hi="PageDown";const ci="PageUp";const ui=" ";const pi="Tab";const fi="Backspace";const mi="Delete";const vi={ArrowDown:ti,ArrowLeft:ii,ArrowRight:si,ArrowUp:ni};function bi(e,t,i){if(i<e){return t}else if(i>t){return e}return i}function gi(e,t,i){return Math.min(Math.max(i,e),t)}function yi(e,t,i=0){[t,i]=[t,i].sort(((e,t)=>e-t));return t<=e&&e<i}const Ci={single:"single",multi:"multi"};class xi extends Fe{constructor(){super(...arguments);this.expandmode=Ci.multi;this.activeItemIndex=0;this.change=()=>{this.$emit("change",this.activeid)};this.setItems=()=>{var e;if(this.accordionItems.length===0){return}this.accordionIds=this.getItemIds();this.accordionItems.forEach(((e,t)=>{if(e instanceof He){e.addEventListener("change",this.activeItemChange);if(this.isSingleExpandMode()){this.activeItemIndex!==t?e.expanded=false:e.expanded=true}}const i=this.accordionIds[t];e.setAttribute("id",typeof i!=="string"?`accordion-${t+1}`:i);this.activeid=this.accordionIds[this.activeItemIndex];e.addEventListener("keydown",this.handleItemKeyDown);e.addEventListener("focus",this.handleItemFocus)}));if(this.isSingleExpandMode()){const t=(e=this.findExpandedItem())!==null&&e!==void 0?e:this.accordionItems[0];t.setAttribute("aria-disabled","true")}};this.removeItemListeners=e=>{e.forEach(((e,t)=>{e.removeEventListener("change",this.activeItemChange);e.removeEventListener("keydown",this.handleItemKeyDown);e.removeEventListener("focus",this.handleItemFocus)}))};this.activeItemChange=e=>{if(e.defaultPrevented||e.target!==e.currentTarget){return}e.preventDefault();const t=e.target;this.activeid=t.getAttribute("id");if(this.isSingleExpandMode()){this.resetItems();t.expanded=true;t.setAttribute("aria-disabled","true");this.accordionItems.forEach((e=>{if(!e.hasAttribute("disabled")&&e.id!==this.activeid){e.removeAttribute("aria-disabled")}}))}this.activeItemIndex=Array.from(this.accordionItems).indexOf(t);this.change()};this.handleItemKeyDown=e=>{if(e.target!==e.currentTarget){return}this.accordionIds=this.getItemIds();switch(e.key){case ni:e.preventDefault();this.adjust(-1);break;case ti:e.preventDefault();this.adjust(1);break;case ai:this.activeItemIndex=0;this.focusItem();break;case li:this.activeItemIndex=this.accordionItems.length-1;this.focusItem();break}};this.handleItemFocus=e=>{if(e.target===e.currentTarget){const t=e.target;const i=this.activeItemIndex=Array.from(this.accordionItems).indexOf(t);if(this.activeItemIndex!==i&&i!==-1){this.activeItemIndex=i;this.activeid=this.accordionIds[this.activeItemIndex]}}}}accordionItemsChanged(e,t){if(this.$fastController.isConnected){this.removeItemListeners(e);this.setItems()}}findExpandedItem(){for(let e=0;e<this.accordionItems.length;e++){if(this.accordionItems[e].getAttribute("expanded")==="true"){return this.accordionItems[e]}}return null}resetItems(){this.accordionItems.forEach(((e,t)=>{e.expanded=false}))}getItemIds(){return this.accordionItems.map((e=>e.getAttribute("id")))}isSingleExpandMode(){return this.expandmode===Ci.single}adjust(e){this.activeItemIndex=bi(0,this.accordionItems.length-1,this.activeItemIndex+e);this.focusItem()}focusItem(){const e=this.accordionItems[this.activeItemIndex];if(e instanceof He){e.expandbutton.focus()}}}f([(0,s.attr)({attribute:"expand-mode"})],xi.prototype,"expandmode",void 0);f([s.observable],xi.prototype,"accordionItems",void 0);const wi=(e,t)=>s.html`
    <a
        class="control"
        part="control"
        download="${e=>e.download}"
        href="${e=>e.href}"
        hreflang="${e=>e.hreflang}"
        ping="${e=>e.ping}"
        referrerpolicy="${e=>e.referrerpolicy}"
        rel="${e=>e.rel}"
        target="${e=>e.target}"
        type="${e=>e.type}"
        aria-atomic="${e=>e.ariaAtomic}"
        aria-busy="${e=>e.ariaBusy}"
        aria-controls="${e=>e.ariaControls}"
        aria-current="${e=>e.ariaCurrent}"
        aria-describedby="${e=>e.ariaDescribedby}"
        aria-details="${e=>e.ariaDetails}"
        aria-disabled="${e=>e.ariaDisabled}"
        aria-errormessage="${e=>e.ariaErrormessage}"
        aria-expanded="${e=>e.ariaExpanded}"
        aria-flowto="${e=>e.ariaFlowto}"
        aria-haspopup="${e=>e.ariaHaspopup}"
        aria-hidden="${e=>e.ariaHidden}"
        aria-invalid="${e=>e.ariaInvalid}"
        aria-keyshortcuts="${e=>e.ariaKeyshortcuts}"
        aria-label="${e=>e.ariaLabel}"
        aria-labelledby="${e=>e.ariaLabelledby}"
        aria-live="${e=>e.ariaLive}"
        aria-owns="${e=>e.ariaOwns}"
        aria-relevant="${e=>e.ariaRelevant}"
        aria-roledescription="${e=>e.ariaRoledescription}"
        ${(0,s.ref)("control")}
    >
        ${r(e,t)}
        <span class="content" part="content">
            <slot ${(0,s.slotted)("defaultSlottedContent")}></slot>
        </span>
        ${o(e,t)}
    </a>
`;class $i{}f([(0,s.attr)({attribute:"aria-atomic"})],$i.prototype,"ariaAtomic",void 0);f([(0,s.attr)({attribute:"aria-busy"})],$i.prototype,"ariaBusy",void 0);f([(0,s.attr)({attribute:"aria-controls"})],$i.prototype,"ariaControls",void 0);f([(0,s.attr)({attribute:"aria-current"})],$i.prototype,"ariaCurrent",void 0);f([(0,s.attr)({attribute:"aria-describedby"})],$i.prototype,"ariaDescribedby",void 0);f([(0,s.attr)({attribute:"aria-details"})],$i.prototype,"ariaDetails",void 0);f([(0,s.attr)({attribute:"aria-disabled"})],$i.prototype,"ariaDisabled",void 0);f([(0,s.attr)({attribute:"aria-errormessage"})],$i.prototype,"ariaErrormessage",void 0);f([(0,s.attr)({attribute:"aria-flowto"})],$i.prototype,"ariaFlowto",void 0);f([(0,s.attr)({attribute:"aria-haspopup"})],$i.prototype,"ariaHaspopup",void 0);f([(0,s.attr)({attribute:"aria-hidden"})],$i.prototype,"ariaHidden",void 0);f([(0,s.attr)({attribute:"aria-invalid"})],$i.prototype,"ariaInvalid",void 0);f([(0,s.attr)({attribute:"aria-keyshortcuts"})],$i.prototype,"ariaKeyshortcuts",void 0);f([(0,s.attr)({attribute:"aria-label"})],$i.prototype,"ariaLabel",void 0);f([(0,s.attr)({attribute:"aria-labelledby"})],$i.prototype,"ariaLabelledby",void 0);f([(0,s.attr)({attribute:"aria-live"})],$i.prototype,"ariaLive",void 0);f([(0,s.attr)({attribute:"aria-owns"})],$i.prototype,"ariaOwns",void 0);f([(0,s.attr)({attribute:"aria-relevant"})],$i.prototype,"ariaRelevant",void 0);f([(0,s.attr)({attribute:"aria-roledescription"})],$i.prototype,"ariaRoledescription",void 0);class ki extends Fe{constructor(){super(...arguments);this.handleUnsupportedDelegatesFocus=()=>{var e;if(window.ShadowRoot&&!window.ShadowRoot.prototype.hasOwnProperty("delegatesFocus")&&((e=this.$fastController.definition.shadowOptions)===null||e===void 0?void 0:e.delegatesFocus)){this.focus=()=>{var e;(e=this.control)===null||e===void 0?void 0:e.focus()}}}}connectedCallback(){super.connectedCallback();this.handleUnsupportedDelegatesFocus()}}f([s.attr],ki.prototype,"download",void 0);f([s.attr],ki.prototype,"href",void 0);f([s.attr],ki.prototype,"hreflang",void 0);f([s.attr],ki.prototype,"ping",void 0);f([s.attr],ki.prototype,"referrerpolicy",void 0);f([s.attr],ki.prototype,"rel",void 0);f([s.attr],ki.prototype,"target",void 0);f([s.attr],ki.prototype,"type",void 0);f([s.observable],ki.prototype,"defaultSlottedContent",void 0);class Ii{}f([(0,s.attr)({attribute:"aria-expanded"})],Ii.prototype,"ariaExpanded",void 0);Me(Ii,$i);Me(ki,n,Ii);const Ei=(e,t)=>s.html`
    <template class="${e=>e.initialLayoutComplete?"loaded":""}">
        ${(0,s.when)((e=>e.initialLayoutComplete),s.html`
                <slot></slot>
            `)}
    </template>
`;var Oi=i(42586);const Ti="abort";const Ri="afterprint";const Si="animationcancel";const Di="animationend";const Ai="animationiteration";const Fi="animationstart";const Li="appinstalled";const Pi="beforeprint";const Mi="beforeunload";const Hi="beginEvent";const zi="blocked";const Vi="blur";const Ni="canplay";const Bi="canplaythrough";const Ui="change";const qi="chargingchange";const ji="chargingtimechange";const _i="click";const Ki="close";const Wi="complete";const Gi="compositionend";const Yi="compositionstart";const Xi="compositionupdate";const Qi="contextmenu";const Zi="copy";const Ji="cut";const es="dblclick";const ts="devicechange";const is="devicemotion";const ss="deviceorientation";const ns="dischargingtimechange";const os="drag";const rs="dragend";const as="dragenter";const ls="dragleave";const ds="dragover";const hs="dragstart";const cs="drop";const us="durationchange";const ps="emptied";const fs="ended";const ms="endevent";const vs="error";const bs="focus";const gs="focusin";const ys="focusout";const Cs="fullscreenchange";const xs="fullscreenerror";const ws="gamepadconnected";const $s="gamepaddisconnected";const ks="gotpointercapture";const Is="hashchange";const Es="lostpointercapture";const Os="input";const Ts="invalid";const Rs="keydown";const Ss="keyup";const Ds="levelchange";const As="load";const Fs="loadeddata";const Ls="loadedmetadata";const Ps="loadend";const Ms="loadstart";const Hs="message";const zs="messageerror";const Vs="mousedown";const Ns="mouseenter";const Bs="mouseleave";const Us="mousemove";const qs="mouseout";const js="mouseover";const _s="mouseup";const Ks="notificationclick";const Ws="offline";const Gs="online";const Ys="open";const Xs="orientationchange";const Qs="pagehide";const Zs="pageshow";const Js="paste";const en="pause";const tn="pointercancel";const sn="pointerdown";const nn="pointerenter";const on="pointerleave";const rn="pointerlockchange";const an="pointerlockerror";const ln="pointermove";const dn="pointerout";const hn="pointerover";const cn="pointerup";const un="play";const pn="playing";const fn="popstate";const mn="progress";const vn="push";const bn="pushsubscriptionchange";const gn="ratechange";const yn="readystatechange";const Cn="repeatevent";const xn="reset";const wn="resize";const $n="resourcetimingbufferfull";const kn="scroll";const In="seeked";const En="seeking";const On="select";const Tn="show";const Rn="slotchange";const Sn="stalled";const Dn="start";const An="storage";const Fn="submit";const Ln="success";const Pn="suspend";const Mn="SVGAbort";const Hn="SVGError";const zn="SVGLoad";const Vn="SVGResize";const Nn="SVGScroll";const Bn="SVGUnload";const Un="SVGZoom";const qn="timeout";const jn="timeupdate";const _n="touchcancel";const Kn="touchend";const Wn="touchmove";const Gn="touchstart";const Yn="transitionend";const Xn="unload";const Qn="upgradeneeded";const Zn="userproximity";const Jn="versionchange";const eo="visibilitychange";const to="volumechange";const io="waiting";const so="wheel";const no=e=>{const t=e.closest("[dir]");return t!==null&&t.dir==="rtl"?Oi.N.rtl:Oi.N.ltr};class oo{constructor(){this.intersectionDetector=null;this.observedElements=new Map;this.requestPosition=(e,t)=>{var i;if(this.intersectionDetector===null){return}if(this.observedElements.has(e)){(i=this.observedElements.get(e))===null||i===void 0?void 0:i.push(t);return}this.observedElements.set(e,[t]);this.intersectionDetector.observe(e)};this.cancelRequestPosition=(e,t)=>{const i=this.observedElements.get(e);if(i!==undefined){const e=i.indexOf(t);if(e!==-1){i.splice(e,1)}}};this.initializeIntersectionDetector=()=>{if(!s.$global.IntersectionObserver){return}this.intersectionDetector=new IntersectionObserver(this.handleIntersection,{root:null,rootMargin:"0px",threshold:[0,1]})};this.handleIntersection=e=>{if(this.intersectionDetector===null){return}const t=[];const i=[];e.forEach((e=>{var s;(s=this.intersectionDetector)===null||s===void 0?void 0:s.unobserve(e.target);const n=this.observedElements.get(e.target);if(n!==undefined){n.forEach((s=>{let n=t.indexOf(s);if(n===-1){n=t.length;t.push(s);i.push([])}i[n].push(e)}));this.observedElements.delete(e.target)}}));t.forEach(((e,t)=>{e(i[t])}))};this.initializeIntersectionDetector()}}class ro extends Fe{constructor(){super(...arguments);this.anchor="";this.viewport="";this.horizontalPositioningMode="uncontrolled";this.horizontalDefaultPosition="unset";this.horizontalViewportLock=false;this.horizontalInset=false;this.horizontalScaling="content";this.verticalPositioningMode="uncontrolled";this.verticalDefaultPosition="unset";this.verticalViewportLock=false;this.verticalInset=false;this.verticalScaling="content";this.fixedPlacement=false;this.autoUpdateMode="anchor";this.anchorElement=null;this.viewportElement=null;this.initialLayoutComplete=false;this.resizeDetector=null;this.baseHorizontalOffset=0;this.baseVerticalOffset=0;this.pendingPositioningUpdate=false;this.pendingReset=false;this.currentDirection=Oi.N.ltr;this.regionVisible=false;this.forceUpdate=false;this.updateThreshold=.5;this.update=()=>{if(!this.pendingPositioningUpdate){this.requestPositionUpdates()}};this.startObservers=()=>{this.stopObservers();if(this.anchorElement===null){return}this.requestPositionUpdates();if(this.resizeDetector!==null){this.resizeDetector.observe(this.anchorElement);this.resizeDetector.observe(this)}};this.requestPositionUpdates=()=>{if(this.anchorElement===null||this.pendingPositioningUpdate){return}ro.intersectionService.requestPosition(this,this.handleIntersection);ro.intersectionService.requestPosition(this.anchorElement,this.handleIntersection);if(this.viewportElement!==null){ro.intersectionService.requestPosition(this.viewportElement,this.handleIntersection)}this.pendingPositioningUpdate=true};this.stopObservers=()=>{if(this.pendingPositioningUpdate){this.pendingPositioningUpdate=false;ro.intersectionService.cancelRequestPosition(this,this.handleIntersection);if(this.anchorElement!==null){ro.intersectionService.cancelRequestPosition(this.anchorElement,this.handleIntersection)}if(this.viewportElement!==null){ro.intersectionService.cancelRequestPosition(this.viewportElement,this.handleIntersection)}}if(this.resizeDetector!==null){this.resizeDetector.disconnect()}};this.getViewport=()=>{if(typeof this.viewport!=="string"||this.viewport===""){return document.documentElement}return document.getElementById(this.viewport)};this.getAnchor=()=>document.getElementById(this.anchor);this.handleIntersection=e=>{if(!this.pendingPositioningUpdate){return}this.pendingPositioningUpdate=false;if(!this.applyIntersectionEntries(e)){return}this.updateLayout()};this.applyIntersectionEntries=e=>{const t=e.find((e=>e.target===this));const i=e.find((e=>e.target===this.anchorElement));const s=e.find((e=>e.target===this.viewportElement));if(t===undefined||s===undefined||i===undefined){return false}if(!this.regionVisible||this.forceUpdate||this.regionRect===undefined||this.anchorRect===undefined||this.viewportRect===undefined||this.isRectDifferent(this.anchorRect,i.boundingClientRect)||this.isRectDifferent(this.viewportRect,s.boundingClientRect)||this.isRectDifferent(this.regionRect,t.boundingClientRect)){this.regionRect=t.boundingClientRect;this.anchorRect=i.boundingClientRect;if(this.viewportElement===document.documentElement){this.viewportRect=new DOMRectReadOnly(s.boundingClientRect.x+document.documentElement.scrollLeft,s.boundingClientRect.y+document.documentElement.scrollTop,s.boundingClientRect.width,s.boundingClientRect.height)}else{this.viewportRect=s.boundingClientRect}this.updateRegionOffset();this.forceUpdate=false;return true}return false};this.updateRegionOffset=()=>{if(this.anchorRect&&this.regionRect){this.baseHorizontalOffset=this.baseHorizontalOffset+(this.anchorRect.left-this.regionRect.left)+(this.translateX-this.baseHorizontalOffset);this.baseVerticalOffset=this.baseVerticalOffset+(this.anchorRect.top-this.regionRect.top)+(this.translateY-this.baseVerticalOffset)}};this.isRectDifferent=(e,t)=>{if(Math.abs(e.top-t.top)>this.updateThreshold||Math.abs(e.right-t.right)>this.updateThreshold||Math.abs(e.bottom-t.bottom)>this.updateThreshold||Math.abs(e.left-t.left)>this.updateThreshold){return true}return false};this.handleResize=e=>{this.update()};this.reset=()=>{if(!this.pendingReset){return}this.pendingReset=false;if(this.anchorElement===null){this.anchorElement=this.getAnchor()}if(this.viewportElement===null){this.viewportElement=this.getViewport()}this.currentDirection=no(this);this.startObservers()};this.updateLayout=()=>{let e=undefined;let t=undefined;if(this.horizontalPositioningMode!=="uncontrolled"){const e=this.getPositioningOptions(this.horizontalInset);if(this.horizontalDefaultPosition==="center"){t="center"}else if(this.horizontalDefaultPosition!=="unset"){let e=this.horizontalDefaultPosition;if(e==="start"||e==="end"){const t=no(this);if(t!==this.currentDirection){this.currentDirection=t;this.initialize();return}if(this.currentDirection===Oi.N.ltr){e=e==="start"?"left":"right"}else{e=e==="start"?"right":"left"}}switch(e){case"left":t=this.horizontalInset?"insetStart":"start";break;case"right":t=this.horizontalInset?"insetEnd":"end";break}}const i=this.horizontalThreshold!==undefined?this.horizontalThreshold:this.regionRect!==undefined?this.regionRect.width:0;const s=this.anchorRect!==undefined?this.anchorRect.left:0;const n=this.anchorRect!==undefined?this.anchorRect.right:0;const o=this.anchorRect!==undefined?this.anchorRect.width:0;const r=this.viewportRect!==undefined?this.viewportRect.left:0;const a=this.viewportRect!==undefined?this.viewportRect.right:0;if(t===undefined||!(this.horizontalPositioningMode==="locktodefault")&&this.getAvailableSpace(t,s,n,o,r,a)<i){t=this.getAvailableSpace(e[0],s,n,o,r,a)>this.getAvailableSpace(e[1],s,n,o,r,a)?e[0]:e[1]}}if(this.verticalPositioningMode!=="uncontrolled"){const t=this.getPositioningOptions(this.verticalInset);if(this.verticalDefaultPosition==="center"){e="center"}else if(this.verticalDefaultPosition!=="unset"){switch(this.verticalDefaultPosition){case"top":e=this.verticalInset?"insetStart":"start";break;case"bottom":e=this.verticalInset?"insetEnd":"end";break}}const i=this.verticalThreshold!==undefined?this.verticalThreshold:this.regionRect!==undefined?this.regionRect.height:0;const s=this.anchorRect!==undefined?this.anchorRect.top:0;const n=this.anchorRect!==undefined?this.anchorRect.bottom:0;const o=this.anchorRect!==undefined?this.anchorRect.height:0;const r=this.viewportRect!==undefined?this.viewportRect.top:0;const a=this.viewportRect!==undefined?this.viewportRect.bottom:0;if(e===undefined||!(this.verticalPositioningMode==="locktodefault")&&this.getAvailableSpace(e,s,n,o,r,a)<i){e=this.getAvailableSpace(t[0],s,n,o,r,a)>this.getAvailableSpace(t[1],s,n,o,r,a)?t[0]:t[1]}}const i=this.getNextRegionDimension(t,e);const s=this.horizontalPosition!==t||this.verticalPosition!==e;this.setHorizontalPosition(t,i);this.setVerticalPosition(e,i);this.updateRegionStyle();if(!this.initialLayoutComplete){this.initialLayoutComplete=true;this.requestPositionUpdates();return}if(!this.regionVisible){this.regionVisible=true;this.style.removeProperty("pointer-events");this.style.removeProperty("opacity");this.classList.toggle("loaded",true);this.$emit("loaded",this,{bubbles:false})}this.updatePositionClasses();if(s){this.$emit("positionchange",this,{bubbles:false})}};this.updateRegionStyle=()=>{this.style.width=this.regionWidth;this.style.height=this.regionHeight;this.style.transform=`translate(${this.translateX}px, ${this.translateY}px)`};this.updatePositionClasses=()=>{this.classList.toggle("top",this.verticalPosition==="start");this.classList.toggle("bottom",this.verticalPosition==="end");this.classList.toggle("inset-top",this.verticalPosition==="insetStart");this.classList.toggle("inset-bottom",this.verticalPosition==="insetEnd");this.classList.toggle("vertical-center",this.verticalPosition==="center");this.classList.toggle("left",this.horizontalPosition==="start");this.classList.toggle("right",this.horizontalPosition==="end");this.classList.toggle("inset-left",this.horizontalPosition==="insetStart");this.classList.toggle("inset-right",this.horizontalPosition==="insetEnd");this.classList.toggle("horizontal-center",this.horizontalPosition==="center")};this.setHorizontalPosition=(e,t)=>{if(e===undefined||this.regionRect===undefined||this.anchorRect===undefined||this.viewportRect===undefined){return}let i=0;switch(this.horizontalScaling){case"anchor":case"fill":i=this.horizontalViewportLock?this.viewportRect.width:t.width;this.regionWidth=`${i}px`;break;case"content":i=this.regionRect.width;this.regionWidth="unset";break}let s=0;switch(e){case"start":this.translateX=this.baseHorizontalOffset-i;if(this.horizontalViewportLock&&this.anchorRect.left>this.viewportRect.right){this.translateX=this.translateX-(this.anchorRect.left-this.viewportRect.right)}break;case"insetStart":this.translateX=this.baseHorizontalOffset-i+this.anchorRect.width;if(this.horizontalViewportLock&&this.anchorRect.right>this.viewportRect.right){this.translateX=this.translateX-(this.anchorRect.right-this.viewportRect.right)}break;case"insetEnd":this.translateX=this.baseHorizontalOffset;if(this.horizontalViewportLock&&this.anchorRect.left<this.viewportRect.left){this.translateX=this.translateX-(this.anchorRect.left-this.viewportRect.left)}break;case"end":this.translateX=this.baseHorizontalOffset+this.anchorRect.width;if(this.horizontalViewportLock&&this.anchorRect.right<this.viewportRect.left){this.translateX=this.translateX-(this.anchorRect.right-this.viewportRect.left)}break;case"center":s=(this.anchorRect.width-i)/2;this.translateX=this.baseHorizontalOffset+s;if(this.horizontalViewportLock){const e=this.anchorRect.left+s;const t=this.anchorRect.right-s;if(e<this.viewportRect.left&&!(t>this.viewportRect.right)){this.translateX=this.translateX-(e-this.viewportRect.left)}else if(t>this.viewportRect.right&&!(e<this.viewportRect.left)){this.translateX=this.translateX-(t-this.viewportRect.right)}}break}this.horizontalPosition=e};this.setVerticalPosition=(e,t)=>{if(e===undefined||this.regionRect===undefined||this.anchorRect===undefined||this.viewportRect===undefined){return}let i=0;switch(this.verticalScaling){case"anchor":case"fill":i=this.verticalViewportLock?this.viewportRect.height:t.height;this.regionHeight=`${i}px`;break;case"content":i=this.regionRect.height;this.regionHeight="unset";break}let s=0;switch(e){case"start":this.translateY=this.baseVerticalOffset-i;if(this.verticalViewportLock&&this.anchorRect.top>this.viewportRect.bottom){this.translateY=this.translateY-(this.anchorRect.top-this.viewportRect.bottom)}break;case"insetStart":this.translateY=this.baseVerticalOffset-i+this.anchorRect.height;if(this.verticalViewportLock&&this.anchorRect.bottom>this.viewportRect.bottom){this.translateY=this.translateY-(this.anchorRect.bottom-this.viewportRect.bottom)}break;case"insetEnd":this.translateY=this.baseVerticalOffset;if(this.verticalViewportLock&&this.anchorRect.top<this.viewportRect.top){this.translateY=this.translateY-(this.anchorRect.top-this.viewportRect.top)}break;case"end":this.translateY=this.baseVerticalOffset+this.anchorRect.height;if(this.verticalViewportLock&&this.anchorRect.bottom<this.viewportRect.top){this.translateY=this.translateY-(this.anchorRect.bottom-this.viewportRect.top)}break;case"center":s=(this.anchorRect.height-i)/2;this.translateY=this.baseVerticalOffset+s;if(this.verticalViewportLock){const e=this.anchorRect.top+s;const t=this.anchorRect.bottom-s;if(e<this.viewportRect.top&&!(t>this.viewportRect.bottom)){this.translateY=this.translateY-(e-this.viewportRect.top)}else if(t>this.viewportRect.bottom&&!(e<this.viewportRect.top)){this.translateY=this.translateY-(t-this.viewportRect.bottom)}}}this.verticalPosition=e};this.getPositioningOptions=e=>{if(e){return["insetStart","insetEnd"]}return["start","end"]};this.getAvailableSpace=(e,t,i,s,n,o)=>{const r=t-n;const a=o-(t+s);switch(e){case"start":return r;case"insetStart":return r+s;case"insetEnd":return a+s;case"end":return a;case"center":return Math.min(r,a)*2+s}};this.getNextRegionDimension=(e,t)=>{const i={height:this.regionRect!==undefined?this.regionRect.height:0,width:this.regionRect!==undefined?this.regionRect.width:0};if(e!==undefined&&this.horizontalScaling==="fill"){i.width=this.getAvailableSpace(e,this.anchorRect!==undefined?this.anchorRect.left:0,this.anchorRect!==undefined?this.anchorRect.right:0,this.anchorRect!==undefined?this.anchorRect.width:0,this.viewportRect!==undefined?this.viewportRect.left:0,this.viewportRect!==undefined?this.viewportRect.right:0)}else if(this.horizontalScaling==="anchor"){i.width=this.anchorRect!==undefined?this.anchorRect.width:0}if(t!==undefined&&this.verticalScaling==="fill"){i.height=this.getAvailableSpace(t,this.anchorRect!==undefined?this.anchorRect.top:0,this.anchorRect!==undefined?this.anchorRect.bottom:0,this.anchorRect!==undefined?this.anchorRect.height:0,this.viewportRect!==undefined?this.viewportRect.top:0,this.viewportRect!==undefined?this.viewportRect.bottom:0)}else if(this.verticalScaling==="anchor"){i.height=this.anchorRect!==undefined?this.anchorRect.height:0}return i};this.startAutoUpdateEventListeners=()=>{window.addEventListener(wn,this.update,{passive:true});window.addEventListener(kn,this.update,{passive:true,capture:true});if(this.resizeDetector!==null&&this.viewportElement!==null){this.resizeDetector.observe(this.viewportElement)}};this.stopAutoUpdateEventListeners=()=>{window.removeEventListener(wn,this.update);window.removeEventListener(kn,this.update);if(this.resizeDetector!==null&&this.viewportElement!==null){this.resizeDetector.unobserve(this.viewportElement)}}}anchorChanged(){if(this.initialLayoutComplete){this.anchorElement=this.getAnchor()}}viewportChanged(){if(this.initialLayoutComplete){this.viewportElement=this.getViewport()}}horizontalPositioningModeChanged(){this.requestReset()}horizontalDefaultPositionChanged(){this.updateForAttributeChange()}horizontalViewportLockChanged(){this.updateForAttributeChange()}horizontalInsetChanged(){this.updateForAttributeChange()}horizontalThresholdChanged(){this.updateForAttributeChange()}horizontalScalingChanged(){this.updateForAttributeChange()}verticalPositioningModeChanged(){this.requestReset()}verticalDefaultPositionChanged(){this.updateForAttributeChange()}verticalViewportLockChanged(){this.updateForAttributeChange()}verticalInsetChanged(){this.updateForAttributeChange()}verticalThresholdChanged(){this.updateForAttributeChange()}verticalScalingChanged(){this.updateForAttributeChange()}fixedPlacementChanged(){if(this.$fastController.isConnected&&this.initialLayoutComplete){this.initialize()}}autoUpdateModeChanged(e,t){if(this.$fastController.isConnected&&this.initialLayoutComplete){if(e==="auto"){this.stopAutoUpdateEventListeners()}if(t==="auto"){this.startAutoUpdateEventListeners()}}}anchorElementChanged(){this.requestReset()}viewportElementChanged(){if(this.$fastController.isConnected&&this.initialLayoutComplete){this.initialize()}}connectedCallback(){super.connectedCallback();if(this.autoUpdateMode==="auto"){this.startAutoUpdateEventListeners()}this.initialize()}disconnectedCallback(){super.disconnectedCallback();if(this.autoUpdateMode==="auto"){this.stopAutoUpdateEventListeners()}this.stopObservers();this.disconnectResizeDetector()}adoptedCallback(){this.initialize()}disconnectResizeDetector(){if(this.resizeDetector!==null){this.resizeDetector.disconnect();this.resizeDetector=null}}initializeResizeDetector(){this.disconnectResizeDetector();this.resizeDetector=new window.ResizeObserver(this.handleResize)}updateForAttributeChange(){if(this.$fastController.isConnected&&this.initialLayoutComplete){this.forceUpdate=true;this.update()}}initialize(){this.initializeResizeDetector();if(this.anchorElement===null){this.anchorElement=this.getAnchor()}this.requestReset()}requestReset(){if(this.$fastController.isConnected&&this.pendingReset===false){this.setInitialState();s.DOM.queueUpdate((()=>this.reset()));this.pendingReset=true}}setInitialState(){this.initialLayoutComplete=false;this.regionVisible=false;this.translateX=0;this.translateY=0;this.baseHorizontalOffset=0;this.baseVerticalOffset=0;this.viewportRect=undefined;this.regionRect=undefined;this.anchorRect=undefined;this.verticalPosition=undefined;this.horizontalPosition=undefined;this.style.opacity="0";this.style.pointerEvents="none";this.forceUpdate=false;this.style.position=this.fixedPlacement?"fixed":"absolute";this.updatePositionClasses();this.updateRegionStyle()}}ro.intersectionService=new oo;f([s.attr],ro.prototype,"anchor",void 0);f([s.attr],ro.prototype,"viewport",void 0);f([(0,s.attr)({attribute:"horizontal-positioning-mode"})],ro.prototype,"horizontalPositioningMode",void 0);f([(0,s.attr)({attribute:"horizontal-default-position"})],ro.prototype,"horizontalDefaultPosition",void 0);f([(0,s.attr)({attribute:"horizontal-viewport-lock",mode:"boolean"})],ro.prototype,"horizontalViewportLock",void 0);f([(0,s.attr)({attribute:"horizontal-inset",mode:"boolean"})],ro.prototype,"horizontalInset",void 0);f([(0,s.attr)({attribute:"horizontal-threshold"})],ro.prototype,"horizontalThreshold",void 0);f([(0,s.attr)({attribute:"horizontal-scaling"})],ro.prototype,"horizontalScaling",void 0);f([(0,s.attr)({attribute:"vertical-positioning-mode"})],ro.prototype,"verticalPositioningMode",void 0);f([(0,s.attr)({attribute:"vertical-default-position"})],ro.prototype,"verticalDefaultPosition",void 0);f([(0,s.attr)({attribute:"vertical-viewport-lock",mode:"boolean"})],ro.prototype,"verticalViewportLock",void 0);f([(0,s.attr)({attribute:"vertical-inset",mode:"boolean"})],ro.prototype,"verticalInset",void 0);f([(0,s.attr)({attribute:"vertical-threshold"})],ro.prototype,"verticalThreshold",void 0);f([(0,s.attr)({attribute:"vertical-scaling"})],ro.prototype,"verticalScaling",void 0);f([(0,s.attr)({attribute:"fixed-placement",mode:"boolean"})],ro.prototype,"fixedPlacement",void 0);f([(0,s.attr)({attribute:"auto-update-mode"})],ro.prototype,"autoUpdateMode",void 0);f([s.observable],ro.prototype,"anchorElement",void 0);f([s.observable],ro.prototype,"viewportElement",void 0);f([s.observable],ro.prototype,"initialLayoutComplete",void 0);const ao={horizontalDefaultPosition:"center",horizontalPositioningMode:"locktodefault",horizontalInset:false,horizontalScaling:"anchor"};const lo=Object.assign(Object.assign({},ao),{verticalDefaultPosition:"top",verticalPositioningMode:"locktodefault",verticalInset:false,verticalScaling:"content"});const ho=Object.assign(Object.assign({},ao),{verticalDefaultPosition:"bottom",verticalPositioningMode:"locktodefault",verticalInset:false,verticalScaling:"content"});const co=Object.assign(Object.assign({},ao),{verticalPositioningMode:"dynamic",verticalInset:false,verticalScaling:"content"});const uo=Object.assign(Object.assign({},lo),{verticalScaling:"fill"});const po=Object.assign(Object.assign({},ho),{verticalScaling:"fill"});const fo=Object.assign(Object.assign({},co),{verticalScaling:"fill"});const mo=(e,t)=>s.html`
    <div
        class="backplate ${e=>e.shape}"
        part="backplate"
        style="${e=>e.fill?`background-color: var(--avatar-fill-${e.fill});`:void 0}"
    >
        <a
            class="link"
            part="link"
            href="${e=>e.link?e.link:void 0}"
            style="${e=>e.color?`color: var(--avatar-color-${e.color});`:void 0}"
        >
            <slot name="media" part="media">${t.media||""}</slot>
            <slot class="content" part="content"><slot>
        </a>
    </div>
    <slot name="badge" part="badge"></slot>
`;class vo extends Fe{connectedCallback(){super.connectedCallback();if(!this.shape){this.shape="circle"}}}f([s.attr],vo.prototype,"fill",void 0);f([s.attr],vo.prototype,"color",void 0);f([s.attr],vo.prototype,"link",void 0);f([s.attr],vo.prototype,"shape",void 0);const bo=(e,t)=>s.html`
    <template class="${e=>e.circular?"circular":""}">
        <div class="control" part="control" style="${e=>e.generateBadgeStyle()}">
            <slot></slot>
        </div>
    </template>
`;class go extends Fe{constructor(){super(...arguments);this.generateBadgeStyle=()=>{if(!this.fill&&!this.color){return}const e=`background-color: var(--badge-fill-${this.fill});`;const t=`color: var(--badge-color-${this.color});`;if(this.fill&&!this.color){return e}else if(this.color&&!this.fill){return t}else{return`${t} ${e}`}}}}f([(0,s.attr)({attribute:"fill"})],go.prototype,"fill",void 0);f([(0,s.attr)({attribute:"color"})],go.prototype,"color",void 0);f([(0,s.attr)({mode:"boolean"})],go.prototype,"circular",void 0);const yo=(e,t)=>s.html`
    <div role="listitem" class="listitem" part="listitem">
        ${(0,s.when)((e=>e.href&&e.href.length>0),s.html`
                ${wi(e,t)}
            `)}
        ${(0,s.when)((e=>!e.href),s.html`
                ${r(e,t)}
                <slot></slot>
                ${o(e,t)}
            `)}
        ${(0,s.when)((e=>e.separator),s.html`
                <span class="separator" part="separator" aria-hidden="true">
                    <slot name="separator">${t.separator||""}</slot>
                </span>
            `)}
    </div>
`;class Co extends ki{constructor(){super(...arguments);this.separator=true}}f([s.observable],Co.prototype,"separator",void 0);Me(Co,n,Ii);const xo=(e,t)=>s.html`
    <template role="navigation">
        <div role="list" class="list" part="list">
            <slot
                ${(0,s.slotted)({property:"slottedBreadcrumbItems",filter:(0,s.elements)()})}
            ></slot>
        </div>
    </template>
`;class wo extends Fe{slottedBreadcrumbItemsChanged(){if(this.$fastController.isConnected){if(this.slottedBreadcrumbItems===undefined||this.slottedBreadcrumbItems.length===0){return}const e=this.slottedBreadcrumbItems[this.slottedBreadcrumbItems.length-1];this.slottedBreadcrumbItems.forEach((t=>{const i=t===e;this.setItemSeparator(t,i);this.setAriaCurrent(t,i)}))}}setItemSeparator(e,t){if(e instanceof Co){e.separator=!t}}findChildWithHref(e){var t,i;if(e.childElementCount>0){return e.querySelector("a[href]")}else if((t=e.shadowRoot)===null||t===void 0?void 0:t.childElementCount){return(i=e.shadowRoot)===null||i===void 0?void 0:i.querySelector("a[href]")}else return null}setAriaCurrent(e,t){const i=this.findChildWithHref(e);if(i===null&&e.hasAttribute("href")&&e instanceof Co){t?e.setAttribute("aria-current","page"):e.removeAttribute("aria-current")}else if(i!==null){t?i.setAttribute("aria-current","page"):i.removeAttribute("aria-current")}}}f([s.observable],wo.prototype,"slottedBreadcrumbItems",void 0);const $o=(e,t)=>s.html`
    <button
        class="control"
        part="control"
        ?autofocus="${e=>e.autofocus}"
        ?disabled="${e=>e.disabled}"
        form="${e=>e.formId}"
        formaction="${e=>e.formaction}"
        formenctype="${e=>e.formenctype}"
        formmethod="${e=>e.formmethod}"
        formnovalidate="${e=>e.formnovalidate}"
        formtarget="${e=>e.formtarget}"
        name="${e=>e.name}"
        type="${e=>e.type}"
        value="${e=>e.value}"
        aria-atomic="${e=>e.ariaAtomic}"
        aria-busy="${e=>e.ariaBusy}"
        aria-controls="${e=>e.ariaControls}"
        aria-current="${e=>e.ariaCurrent}"
        aria-describedby="${e=>e.ariaDescribedby}"
        aria-details="${e=>e.ariaDetails}"
        aria-disabled="${e=>e.ariaDisabled}"
        aria-errormessage="${e=>e.ariaErrormessage}"
        aria-expanded="${e=>e.ariaExpanded}"
        aria-flowto="${e=>e.ariaFlowto}"
        aria-haspopup="${e=>e.ariaHaspopup}"
        aria-hidden="${e=>e.ariaHidden}"
        aria-invalid="${e=>e.ariaInvalid}"
        aria-keyshortcuts="${e=>e.ariaKeyshortcuts}"
        aria-label="${e=>e.ariaLabel}"
        aria-labelledby="${e=>e.ariaLabelledby}"
        aria-live="${e=>e.ariaLive}"
        aria-owns="${e=>e.ariaOwns}"
        aria-pressed="${e=>e.ariaPressed}"
        aria-relevant="${e=>e.ariaRelevant}"
        aria-roledescription="${e=>e.ariaRoledescription}"
        ${(0,s.ref)("control")}
    >
        ${r(e,t)}
        <span class="content" part="content">
            <slot ${(0,s.slotted)("defaultSlottedContent")}></slot>
        </span>
        ${o(e,t)}
    </button>
`;const ko="form-associated-proxy";const Io="ElementInternals";const Eo=Io in window&&"setFormValue"in window[Io].prototype;const Oo=new WeakMap;function To(e){const t=class extends e{constructor(...e){super(...e);this.dirtyValue=false;this.disabled=false;this.proxyEventsToBlock=["change","click"];this.proxyInitialized=false;this.required=false;this.initialValue=this.initialValue||"";if(!this.elementInternals){this.formResetCallback=this.formResetCallback.bind(this)}}static get formAssociated(){return Eo}get validity(){return this.elementInternals?this.elementInternals.validity:this.proxy.validity}get form(){return this.elementInternals?this.elementInternals.form:this.proxy.form}get validationMessage(){return this.elementInternals?this.elementInternals.validationMessage:this.proxy.validationMessage}get willValidate(){return this.elementInternals?this.elementInternals.willValidate:this.proxy.willValidate}get labels(){if(this.elementInternals){return Object.freeze(Array.from(this.elementInternals.labels))}else if(this.proxy instanceof HTMLElement&&this.proxy.ownerDocument&&this.id){const e=this.proxy.labels;const t=Array.from(this.proxy.getRootNode().querySelectorAll(`[for='${this.id}']`));const i=e?t.concat(Array.from(e)):t;return Object.freeze(i)}else{return s.emptyArray}}valueChanged(e,t){this.dirtyValue=true;if(this.proxy instanceof HTMLElement){this.proxy.value=this.value}this.currentValue=this.value;this.setFormValue(this.value);this.validate()}currentValueChanged(){this.value=this.currentValue}initialValueChanged(e,t){if(!this.dirtyValue){this.value=this.initialValue;this.dirtyValue=false}}disabledChanged(e,t){if(this.proxy instanceof HTMLElement){this.proxy.disabled=this.disabled}s.DOM.queueUpdate((()=>this.classList.toggle("disabled",this.disabled)))}nameChanged(e,t){if(this.proxy instanceof HTMLElement){this.proxy.name=this.name}}requiredChanged(e,t){if(this.proxy instanceof HTMLElement){this.proxy.required=this.required}s.DOM.queueUpdate((()=>this.classList.toggle("required",this.required)));this.validate()}get elementInternals(){if(!Eo){return null}let e=Oo.get(this);if(!e){e=this.attachInternals();Oo.set(this,e)}return e}connectedCallback(){super.connectedCallback();this.addEventListener("keypress",this._keypressHandler);if(!this.value){this.value=this.initialValue;this.dirtyValue=false}if(!this.elementInternals){this.attachProxy();if(this.form){this.form.addEventListener("reset",this.formResetCallback)}}}disconnectedCallback(){super.disconnectedCallback();this.proxyEventsToBlock.forEach((e=>this.proxy.removeEventListener(e,this.stopPropagation)));if(!this.elementInternals&&this.form){this.form.removeEventListener("reset",this.formResetCallback)}}checkValidity(){return this.elementInternals?this.elementInternals.checkValidity():this.proxy.checkValidity()}reportValidity(){return this.elementInternals?this.elementInternals.reportValidity():this.proxy.reportValidity()}setValidity(e,t,i){if(this.elementInternals){this.elementInternals.setValidity(e,t,i)}else if(typeof t==="string"){this.proxy.setCustomValidity(t)}}formDisabledCallback(e){this.disabled=e}formResetCallback(){this.value=this.initialValue;this.dirtyValue=false}attachProxy(){var e;if(!this.proxyInitialized){this.proxyInitialized=true;this.proxy.style.display="none";this.proxyEventsToBlock.forEach((e=>this.proxy.addEventListener(e,this.stopPropagation)));this.proxy.disabled=this.disabled;this.proxy.required=this.required;if(typeof this.name==="string"){this.proxy.name=this.name}if(typeof this.value==="string"){this.proxy.value=this.value}this.proxy.setAttribute("slot",ko);this.proxySlot=document.createElement("slot");this.proxySlot.setAttribute("name",ko)}(e=this.shadowRoot)===null||e===void 0?void 0:e.appendChild(this.proxySlot);this.appendChild(this.proxy)}detachProxy(){var e;this.removeChild(this.proxy);(e=this.shadowRoot)===null||e===void 0?void 0:e.removeChild(this.proxySlot)}validate(e){if(this.proxy instanceof HTMLElement){this.setValidity(this.proxy.validity,this.proxy.validationMessage,e)}}setFormValue(e,t){if(this.elementInternals){this.elementInternals.setFormValue(e,t||e)}}_keypressHandler(e){switch(e.key){case oi:if(this.form instanceof HTMLFormElement){const e=this.form.querySelector("[type=submit]");e===null||e===void 0?void 0:e.click()}break}}stopPropagation(e){e.stopPropagation()}};(0,s.attr)({mode:"boolean"})(t.prototype,"disabled");(0,s.attr)({mode:"fromView",attribute:"value"})(t.prototype,"initialValue");(0,s.attr)({attribute:"current-value"})(t.prototype,"currentValue");(0,s.attr)(t.prototype,"name");(0,s.attr)({mode:"boolean"})(t.prototype,"required");(0,s.observable)(t.prototype,"value");return t}function Ro(e){class t extends(To(e)){}class i extends t{constructor(...e){super(e);this.dirtyChecked=false;this.checkedAttribute=false;this.checked=false;this.dirtyChecked=false}checkedAttributeChanged(){this.defaultChecked=this.checkedAttribute}defaultCheckedChanged(){if(!this.dirtyChecked){this.checked=this.defaultChecked;this.dirtyChecked=false}}checkedChanged(e,t){if(!this.dirtyChecked){this.dirtyChecked=true}this.currentChecked=this.checked;this.updateForm();if(this.proxy instanceof HTMLInputElement){this.proxy.checked=this.checked}if(e!==undefined){this.$emit("change")}this.validate()}currentCheckedChanged(e,t){this.checked=this.currentChecked}updateForm(){const e=this.checked?this.value:null;this.setFormValue(e,e)}connectedCallback(){super.connectedCallback();this.updateForm()}formResetCallback(){super.formResetCallback();this.checked=!!this.checkedAttribute;this.dirtyChecked=false}}(0,s.attr)({attribute:"checked",mode:"boolean"})(i.prototype,"checkedAttribute");(0,s.attr)({attribute:"current-checked",converter:s.booleanConverter})(i.prototype,"currentChecked");(0,s.observable)(i.prototype,"defaultChecked");(0,s.observable)(i.prototype,"checked");return i}class So extends Fe{}class Do extends(To(So)){constructor(){super(...arguments);this.proxy=document.createElement("input")}}class Ao extends Do{constructor(){super(...arguments);this.handleClick=e=>{var t;if(this.disabled&&((t=this.defaultSlottedContent)===null||t===void 0?void 0:t.length)<=1){e.stopPropagation()}};this.handleSubmission=()=>{if(!this.form){return}const e=this.proxy.isConnected;if(!e){this.attachProxy()}typeof this.form.requestSubmit==="function"?this.form.requestSubmit(this.proxy):this.proxy.click();if(!e){this.detachProxy()}};this.handleFormReset=()=>{var e;(e=this.form)===null||e===void 0?void 0:e.reset()};this.handleUnsupportedDelegatesFocus=()=>{var e;if(window.ShadowRoot&&!window.ShadowRoot.prototype.hasOwnProperty("delegatesFocus")&&((e=this.$fastController.definition.shadowOptions)===null||e===void 0?void 0:e.delegatesFocus)){this.focus=()=>{this.control.focus()}}}}formactionChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.formAction=this.formaction}}formenctypeChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.formEnctype=this.formenctype}}formmethodChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.formMethod=this.formmethod}}formnovalidateChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.formNoValidate=this.formnovalidate}}formtargetChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.formTarget=this.formtarget}}typeChanged(e,t){if(this.proxy instanceof HTMLInputElement){this.proxy.type=this.type}t==="submit"&&this.addEventListener("click",this.handleSubmission);e==="submit"&&this.removeEventListener("click",this.handleSubmission);t==="reset"&&this.addEventListener("click",this.handleFormReset);e==="reset"&&this.removeEventListener("click",this.handleFormReset)}validate(){super.validate(this.control)}connectedCallback(){var e;super.connectedCallback();this.proxy.setAttribute("type",this.type);this.handleUnsupportedDelegatesFocus();const t=Array.from((e=this.control)===null||e===void 0?void 0:e.children);if(t){t.forEach((e=>{e.addEventListener("click",this.handleClick)}))}}disconnectedCallback(){var e;super.disconnectedCallback();const t=Array.from((e=this.control)===null||e===void 0?void 0:e.children);if(t){t.forEach((e=>{e.removeEventListener("click",this.handleClick)}))}}}f([(0,s.attr)({mode:"boolean"})],Ao.prototype,"autofocus",void 0);f([(0,s.attr)({attribute:"form"})],Ao.prototype,"formId",void 0);f([s.attr],Ao.prototype,"formaction",void 0);f([s.attr],Ao.prototype,"formenctype",void 0);f([s.attr],Ao.prototype,"formmethod",void 0);f([(0,s.attr)({mode:"boolean"})],Ao.prototype,"formnovalidate",void 0);f([s.attr],Ao.prototype,"formtarget",void 0);f([s.attr],Ao.prototype,"type",void 0);f([s.observable],Ao.prototype,"defaultSlottedContent",void 0);class Fo{}f([(0,s.attr)({attribute:"aria-expanded"})],Fo.prototype,"ariaExpanded",void 0);f([(0,s.attr)({attribute:"aria-pressed"})],Fo.prototype,"ariaPressed",void 0);Me(Fo,$i);Me(Ao,n,Fo);class Lo{constructor(e){this.dayFormat="numeric";this.weekdayFormat="long";this.monthFormat="long";this.yearFormat="numeric";this.date=new Date;if(e){for(const t in e){const i=e[t];if(t==="date"){this.date=this.getDateObject(i)}else{this[t]=i}}}}getDateObject(e){if(typeof e==="string"){const t=e.split(/[/-]/);if(t.length<3){return new Date}return new Date(parseInt(t[2],10),parseInt(t[0],10)-1,parseInt(t[1],10))}else if("day"in e&&"month"in e&&"year"in e){const{day:t,month:i,year:s}=e;return new Date(s,i-1,t)}return e}getDate(e=this.date,t={weekday:this.weekdayFormat,month:this.monthFormat,day:this.dayFormat,year:this.yearFormat},i=this.locale){const s=this.getDateObject(e);if(!s.getTime()){return""}const n=Object.assign({timeZone:Intl.DateTimeFormat().resolvedOptions().timeZone},t);return new Intl.DateTimeFormat(i,n).format(s)}getDay(e=this.date.getDate(),t=this.dayFormat,i=this.locale){return this.getDate({month:1,day:e,year:2020},{day:t},i)}getMonth(e=this.date.getMonth()+1,t=this.monthFormat,i=this.locale){return this.getDate({month:e,day:2,year:2020},{month:t},i)}getYear(e=this.date.getFullYear(),t=this.yearFormat,i=this.locale){return this.getDate({month:2,day:2,year:e},{year:t},i)}getWeekday(e=0,t=this.weekdayFormat,i=this.locale){const s=`1-${e+1}-2017`;return this.getDate(s,{weekday:t},i)}getWeekdays(e=this.weekdayFormat,t=this.locale){return Array(7).fill(null).map(((i,s)=>this.getWeekday(s,e,t)))}}class Po extends Fe{constructor(){super(...arguments);this.dateFormatter=new Lo;this.readonly=false;this.locale="en-US";this.month=(new Date).getMonth()+1;this.year=(new Date).getFullYear();this.dayFormat="numeric";this.weekdayFormat="short";this.monthFormat="long";this.yearFormat="numeric";this.minWeeks=0;this.disabledDates="";this.selectedDates="";this.oneDayInMs=864e5}localeChanged(){this.dateFormatter.locale=this.locale}dayFormatChanged(){this.dateFormatter.dayFormat=this.dayFormat}weekdayFormatChanged(){this.dateFormatter.weekdayFormat=this.weekdayFormat}monthFormatChanged(){this.dateFormatter.monthFormat=this.monthFormat}yearFormatChanged(){this.dateFormatter.yearFormat=this.yearFormat}getMonthInfo(e=this.month,t=this.year){const i=e=>new Date(e.getFullYear(),e.getMonth(),1).getDay();const s=e=>{const t=new Date(e.getFullYear(),e.getMonth()+1,1);return new Date(t.getTime()-this.oneDayInMs).getDate()};const n=new Date(t,e-1);const o=new Date(t,e);const r=new Date(t,e-2);return{length:s(n),month:e,start:i(n),year:t,previous:{length:s(r),month:r.getMonth()+1,start:i(r),year:r.getFullYear()},next:{length:s(o),month:o.getMonth()+1,start:i(o),year:o.getFullYear()}}}getDays(e=this.getMonthInfo(),t=this.minWeeks){t=t>10?10:t;const{start:i,length:s,previous:n,next:o}=e;const r=[];let a=1-i;while(a<s+1||r.length<t||r[r.length-1].length%7!==0){const{month:t,year:i}=a<1?n:a>s?o:e;const l=a<1?n.length+a:a>s?a-s:a;const d=`${t}-${l}-${i}`;const h=this.dateInString(d,this.disabledDates);const c=this.dateInString(d,this.selectedDates);const u={day:l,month:t,year:i,disabled:h,selected:c};const p=r[r.length-1];if(r.length===0||p.length%7===0){r.push([u])}else{p.push(u)}a++}return r}dateInString(e,t){const i=t.split(",").map((e=>e.trim()));e=typeof e==="string"?e:`${e.getMonth()+1}-${e.getDate()}-${e.getFullYear()}`;return i.some((t=>t===e))}getDayClassNames(e,t){const{day:i,month:s,year:n,disabled:o,selected:r}=e;const a=t===`${s}-${i}-${n}`;const l=this.month!==s;return["day",a&&"today",l&&"inactive",o&&"disabled",r&&"selected"].filter(Boolean).join(" ")}getWeekdayText(){const e=this.dateFormatter.getWeekdays().map((e=>({text:e})));if(this.weekdayFormat!=="long"){const t=this.dateFormatter.getWeekdays("long");e.forEach(((e,i)=>{e.abbr=t[i]}))}return e}handleDateSelect(e,t){e.preventDefault;this.$emit("dateselected",t)}handleKeydown(e,t){if(e.key===oi){this.handleDateSelect(e,t)}return true}}f([(0,s.attr)({mode:"boolean"})],Po.prototype,"readonly",void 0);f([s.attr],Po.prototype,"locale",void 0);f([(0,s.attr)({converter:s.nullableNumberConverter})],Po.prototype,"month",void 0);f([(0,s.attr)({converter:s.nullableNumberConverter})],Po.prototype,"year",void 0);f([(0,s.attr)({attribute:"day-format",mode:"fromView"})],Po.prototype,"dayFormat",void 0);f([(0,s.attr)({attribute:"weekday-format",mode:"fromView"})],Po.prototype,"weekdayFormat",void 0);f([(0,s.attr)({attribute:"month-format",mode:"fromView"})],Po.prototype,"monthFormat",void 0);f([(0,s.attr)({attribute:"year-format",mode:"fromView"})],Po.prototype,"yearFormat",void 0);f([(0,s.attr)({attribute:"min-weeks",converter:s.nullableNumberConverter})],Po.prototype,"minWeeks",void 0);f([(0,s.attr)({attribute:"disabled-dates"})],Po.prototype,"disabledDates",void 0);f([(0,s.attr)({attribute:"selected-dates"})],Po.prototype,"selectedDates",void 0);const Mo={none:"none",default:"default",sticky:"sticky"};const Ho={default:"default",columnHeader:"columnheader",rowHeader:"rowheader"};const zo={default:"default",header:"header",stickyHeader:"sticky-header"};const Vo=s.html`
    <template>
        ${e=>e.rowData===null||e.columnDefinition===null||e.columnDefinition.columnDataKey===null?null:e.rowData[e.columnDefinition.columnDataKey]}
    </template>
`;const No=s.html`
    <template>
        ${e=>e.columnDefinition===null?null:e.columnDefinition.title===undefined?e.columnDefinition.columnDataKey:e.columnDefinition.title}
    </template>
`;class Bo extends Fe{constructor(){super(...arguments);this.cellType=Ho["default"];this.rowData=null;this.columnDefinition=null;this.isActiveCell=false;this.customCellView=null;this.updateCellStyle=()=>{this.style.gridColumn=this.gridColumn}}cellTypeChanged(){if(this.$fastController.isConnected){this.updateCellView()}}gridColumnChanged(){if(this.$fastController.isConnected){this.updateCellStyle()}}columnDefinitionChanged(e,t){if(this.$fastController.isConnected){this.updateCellView()}}connectedCallback(){var e;super.connectedCallback();this.addEventListener(gs,this.handleFocusin);this.addEventListener(ys,this.handleFocusout);this.addEventListener(Rs,this.handleKeydown);this.style.gridColumn=`${((e=this.columnDefinition)===null||e===void 0?void 0:e.gridColumn)===undefined?0:this.columnDefinition.gridColumn}`;this.updateCellView();this.updateCellStyle()}disconnectedCallback(){super.disconnectedCallback();this.removeEventListener(gs,this.handleFocusin);this.removeEventListener(ys,this.handleFocusout);this.removeEventListener(Rs,this.handleKeydown);this.disconnectCellView()}handleFocusin(e){if(this.isActiveCell){return}this.isActiveCell=true;switch(this.cellType){case Ho.columnHeader:if(this.columnDefinition!==null&&this.columnDefinition.headerCellInternalFocusQueue!==true&&typeof this.columnDefinition.headerCellFocusTargetCallback==="function"){const e=this.columnDefinition.headerCellFocusTargetCallback(this);if(e!==null){e.focus()}}break;default:if(this.columnDefinition!==null&&this.columnDefinition.cellInternalFocusQueue!==true&&typeof this.columnDefinition.cellFocusTargetCallback==="function"){const e=this.columnDefinition.cellFocusTargetCallback(this);if(e!==null){e.focus()}}break}this.$emit("cell-focused",this)}handleFocusout(e){if(this!==document.activeElement&&!this.contains(document.activeElement)){this.isActiveCell=false}}handleKeydown(e){if(e.defaultPrevented||this.columnDefinition===null||this.cellType===Ho["default"]&&this.columnDefinition.cellInternalFocusQueue!==true||this.cellType===Ho.columnHeader&&this.columnDefinition.headerCellInternalFocusQueue!==true){return}switch(e.key){case oi:case di:if(this.contains(document.activeElement)&&document.activeElement!==this){return}switch(this.cellType){case Ho.columnHeader:if(this.columnDefinition.headerCellFocusTargetCallback!==undefined){const t=this.columnDefinition.headerCellFocusTargetCallback(this);if(t!==null){t.focus()}e.preventDefault()}break;default:if(this.columnDefinition.cellFocusTargetCallback!==undefined){const t=this.columnDefinition.cellFocusTargetCallback(this);if(t!==null){t.focus()}e.preventDefault()}break}break;case ri:if(this.contains(document.activeElement)&&document.activeElement!==this){this.focus();e.preventDefault()}break}}updateCellView(){this.disconnectCellView();if(this.columnDefinition===null){return}switch(this.cellType){case Ho.columnHeader:if(this.columnDefinition.headerCellTemplate!==undefined){this.customCellView=this.columnDefinition.headerCellTemplate.render(this,this)}else{this.customCellView=No.render(this,this)}break;case undefined:case Ho.rowHeader:case Ho["default"]:if(this.columnDefinition.cellTemplate!==undefined){this.customCellView=this.columnDefinition.cellTemplate.render(this,this)}else{this.customCellView=Vo.render(this,this)}break}}disconnectCellView(){if(this.customCellView!==null){this.customCellView.dispose();this.customCellView=null}}}f([(0,s.attr)({attribute:"cell-type"})],Bo.prototype,"cellType",void 0);f([(0,s.attr)({attribute:"grid-column"})],Bo.prototype,"gridColumn",void 0);f([s.observable],Bo.prototype,"rowData",void 0);f([s.observable],Bo.prototype,"columnDefinition",void 0);class Uo extends Fe{constructor(){super(...arguments);this.rowType=zo["default"];this.rowData=null;this.columnDefinitions=null;this.isActiveRow=false;this.cellsRepeatBehavior=null;this.cellsPlaceholder=null;this.focusColumnIndex=0;this.refocusOnLoad=false;this.updateRowStyle=()=>{this.style.gridTemplateColumns=this.gridTemplateColumns}}gridTemplateColumnsChanged(){if(this.$fastController.isConnected){this.updateRowStyle()}}rowTypeChanged(){if(this.$fastController.isConnected){this.updateItemTemplate()}}rowDataChanged(){if(this.rowData!==null&&this.isActiveRow){this.refocusOnLoad=true;return}}cellItemTemplateChanged(){this.updateItemTemplate()}headerCellItemTemplateChanged(){this.updateItemTemplate()}connectedCallback(){super.connectedCallback();if(this.cellsRepeatBehavior===null){this.cellsPlaceholder=document.createComment("");this.appendChild(this.cellsPlaceholder);this.updateItemTemplate();this.cellsRepeatBehavior=new s.RepeatDirective((e=>e.columnDefinitions),(e=>e.activeCellItemTemplate),{positioning:true}).createBehavior(this.cellsPlaceholder);this.$fastController.addBehaviors([this.cellsRepeatBehavior])}this.addEventListener("cell-focused",this.handleCellFocus);this.addEventListener(ys,this.handleFocusout);this.addEventListener(Rs,this.handleKeydown);this.updateRowStyle();if(this.refocusOnLoad){this.refocusOnLoad=false;if(this.cellElements.length>this.focusColumnIndex){this.cellElements[this.focusColumnIndex].focus()}}}disconnectedCallback(){super.disconnectedCallback();this.removeEventListener("cell-focused",this.handleCellFocus);this.removeEventListener(ys,this.handleFocusout);this.removeEventListener(Rs,this.handleKeydown)}handleFocusout(e){if(!this.contains(e.target)){this.isActiveRow=false;this.focusColumnIndex=0}}handleCellFocus(e){this.isActiveRow=true;this.focusColumnIndex=this.cellElements.indexOf(e.target);this.$emit("row-focused",this)}handleKeydown(e){if(e.defaultPrevented){return}let t=0;switch(e.key){case ii:t=Math.max(0,this.focusColumnIndex-1);this.cellElements[t].focus();e.preventDefault();break;case si:t=Math.min(this.cellElements.length-1,this.focusColumnIndex+1);this.cellElements[t].focus();e.preventDefault();break;case ai:if(!e.ctrlKey){this.cellElements[0].focus();e.preventDefault()}break;case li:if(!e.ctrlKey){this.cellElements[this.cellElements.length-1].focus();e.preventDefault()}break}}updateItemTemplate(){this.activeCellItemTemplate=this.rowType===zo["default"]&&this.cellItemTemplate!==undefined?this.cellItemTemplate:this.rowType===zo["default"]&&this.cellItemTemplate===undefined?this.defaultCellItemTemplate:this.headerCellItemTemplate!==undefined?this.headerCellItemTemplate:this.defaultHeaderCellItemTemplate}}f([(0,s.attr)({attribute:"grid-template-columns"})],Uo.prototype,"gridTemplateColumns",void 0);f([(0,s.attr)({attribute:"row-type"})],Uo.prototype,"rowType",void 0);f([s.observable],Uo.prototype,"rowData",void 0);f([s.observable],Uo.prototype,"columnDefinitions",void 0);f([s.observable],Uo.prototype,"cellItemTemplate",void 0);f([s.observable],Uo.prototype,"headerCellItemTemplate",void 0);f([s.observable],Uo.prototype,"rowIndex",void 0);f([s.observable],Uo.prototype,"isActiveRow",void 0);f([s.observable],Uo.prototype,"activeCellItemTemplate",void 0);f([s.observable],Uo.prototype,"defaultCellItemTemplate",void 0);f([s.observable],Uo.prototype,"defaultHeaderCellItemTemplate",void 0);f([s.observable],Uo.prototype,"cellElements",void 0);class qo extends Fe{constructor(){super();this.noTabbing=false;this.generateHeader=Mo["default"];this.rowsData=[];this.columnDefinitions=null;this.focusRowIndex=0;this.focusColumnIndex=0;this.rowsPlaceholder=null;this.generatedHeader=null;this.isUpdatingFocus=false;this.pendingFocusUpdate=false;this.rowindexUpdateQueued=false;this.columnDefinitionsStale=true;this.generatedGridTemplateColumns="";this.focusOnCell=(e,t,i)=>{if(this.rowElements.length===0){this.focusRowIndex=0;this.focusColumnIndex=0;return}const s=Math.max(0,Math.min(this.rowElements.length-1,e));const n=this.rowElements[s];const o=n.querySelectorAll('[role="cell"], [role="gridcell"], [role="columnheader"], [role="rowheader"]');const r=Math.max(0,Math.min(o.length-1,t));const a=o[r];if(i&&this.scrollHeight!==this.clientHeight&&(s<this.focusRowIndex&&this.scrollTop>0||s>this.focusRowIndex&&this.scrollTop<this.scrollHeight-this.clientHeight)){a.scrollIntoView({block:"center",inline:"center"})}a.focus()};this.onChildListChange=(e,t)=>{if(e&&e.length){e.forEach((e=>{e.addedNodes.forEach((e=>{if(e.nodeType===1&&e.getAttribute("role")==="row"){e.columnDefinitions=this.columnDefinitions}}))}));this.queueRowIndexUpdate()}};this.queueRowIndexUpdate=()=>{if(!this.rowindexUpdateQueued){this.rowindexUpdateQueued=true;s.DOM.queueUpdate(this.updateRowIndexes)}};this.updateRowIndexes=()=>{let e=this.gridTemplateColumns;if(e===undefined){if(this.generatedGridTemplateColumns===""&&this.rowElements.length>0){const e=this.rowElements[0];this.generatedGridTemplateColumns=new Array(e.cellElements.length).fill("1fr").join(" ")}e=this.generatedGridTemplateColumns}this.rowElements.forEach(((t,i)=>{const s=t;s.rowIndex=i;s.gridTemplateColumns=e;if(this.columnDefinitionsStale){s.columnDefinitions=this.columnDefinitions}}));this.rowindexUpdateQueued=false;this.columnDefinitionsStale=false}}static generateTemplateColumns(e){let t="";e.forEach((e=>{t=`${t}${t===""?"":" "}${"1fr"}`}));return t}noTabbingChanged(){if(this.$fastController.isConnected){if(this.noTabbing){this.setAttribute("tabIndex","-1")}else{this.setAttribute("tabIndex",this.contains(document.activeElement)||this===document.activeElement?"-1":"0")}}}generateHeaderChanged(){if(this.$fastController.isConnected){this.toggleGeneratedHeader()}}gridTemplateColumnsChanged(){if(this.$fastController.isConnected){this.updateRowIndexes()}}rowsDataChanged(){if(this.columnDefinitions===null&&this.rowsData.length>0){this.columnDefinitions=qo.generateColumns(this.rowsData[0])}if(this.$fastController.isConnected){this.toggleGeneratedHeader()}}columnDefinitionsChanged(){if(this.columnDefinitions===null){this.generatedGridTemplateColumns="";return}this.generatedGridTemplateColumns=qo.generateTemplateColumns(this.columnDefinitions);if(this.$fastController.isConnected){this.columnDefinitionsStale=true;this.queueRowIndexUpdate()}}headerCellItemTemplateChanged(){if(this.$fastController.isConnected){if(this.generatedHeader!==null){this.generatedHeader.headerCellItemTemplate=this.headerCellItemTemplate}}}focusRowIndexChanged(){if(this.$fastController.isConnected){this.queueFocusUpdate()}}focusColumnIndexChanged(){if(this.$fastController.isConnected){this.queueFocusUpdate()}}connectedCallback(){super.connectedCallback();if(this.rowItemTemplate===undefined){this.rowItemTemplate=this.defaultRowItemTemplate}this.rowsPlaceholder=document.createComment("");this.appendChild(this.rowsPlaceholder);this.toggleGeneratedHeader();this.rowsRepeatBehavior=new s.RepeatDirective((e=>e.rowsData),(e=>e.rowItemTemplate),{positioning:true}).createBehavior(this.rowsPlaceholder);this.$fastController.addBehaviors([this.rowsRepeatBehavior]);this.addEventListener("row-focused",this.handleRowFocus);this.addEventListener(bs,this.handleFocus);this.addEventListener(Rs,this.handleKeydown);this.addEventListener(ys,this.handleFocusOut);this.observer=new MutationObserver(this.onChildListChange);this.observer.observe(this,{childList:true});if(this.noTabbing){this.setAttribute("tabindex","-1")}s.DOM.queueUpdate(this.queueRowIndexUpdate)}disconnectedCallback(){super.disconnectedCallback();this.removeEventListener("row-focused",this.handleRowFocus);this.removeEventListener(bs,this.handleFocus);this.removeEventListener(Rs,this.handleKeydown);this.removeEventListener(ys,this.handleFocusOut);this.observer.disconnect();this.rowsPlaceholder=null;this.generatedHeader=null}handleRowFocus(e){this.isUpdatingFocus=true;const t=e.target;this.focusRowIndex=this.rowElements.indexOf(t);this.focusColumnIndex=t.focusColumnIndex;this.setAttribute("tabIndex","-1");this.isUpdatingFocus=false}handleFocus(e){this.focusOnCell(this.focusRowIndex,this.focusColumnIndex,true)}handleFocusOut(e){if(e.relatedTarget===null||!this.contains(e.relatedTarget)){this.setAttribute("tabIndex",this.noTabbing?"-1":"0")}}handleKeydown(e){if(e.defaultPrevented){return}let t;const i=this.rowElements.length-1;const s=this.offsetHeight+this.scrollTop;const n=this.rowElements[i];switch(e.key){case ni:e.preventDefault();this.focusOnCell(this.focusRowIndex-1,this.focusColumnIndex,true);break;case ti:e.preventDefault();this.focusOnCell(this.focusRowIndex+1,this.focusColumnIndex,true);break;case ci:e.preventDefault();if(this.rowElements.length===0){this.focusOnCell(0,0,false);break}if(this.focusRowIndex===0){this.focusOnCell(0,this.focusColumnIndex,false);return}t=this.focusRowIndex-1;for(t;t>=0;t--){const e=this.rowElements[t];if(e.offsetTop<this.scrollTop){this.scrollTop=e.offsetTop+e.clientHeight-this.clientHeight;break}}this.focusOnCell(t,this.focusColumnIndex,false);break;case hi:e.preventDefault();if(this.rowElements.length===0){this.focusOnCell(0,0,false);break}if(this.focusRowIndex>=i||n.offsetTop+n.offsetHeight<=s){this.focusOnCell(i,this.focusColumnIndex,false);return}t=this.focusRowIndex+1;for(t;t<=i;t++){const e=this.rowElements[t];if(e.offsetTop+e.offsetHeight>s){let t=0;if(this.generateHeader===Mo.sticky&&this.generatedHeader!==null){t=this.generatedHeader.clientHeight}this.scrollTop=e.offsetTop-t;break}}this.focusOnCell(t,this.focusColumnIndex,false);break;case ai:if(e.ctrlKey){e.preventDefault();this.focusOnCell(0,0,true)}break;case li:if(e.ctrlKey&&this.columnDefinitions!==null){e.preventDefault();this.focusOnCell(this.rowElements.length-1,this.columnDefinitions.length-1,true)}break}}queueFocusUpdate(){if(this.isUpdatingFocus&&(this.contains(document.activeElement)||this===document.activeElement)){return}if(this.pendingFocusUpdate===false){this.pendingFocusUpdate=true;s.DOM.queueUpdate((()=>this.updateFocus()))}}updateFocus(){this.pendingFocusUpdate=false;this.focusOnCell(this.focusRowIndex,this.focusColumnIndex,true)}toggleGeneratedHeader(){if(this.generatedHeader!==null){this.removeChild(this.generatedHeader);this.generatedHeader=null}if(this.generateHeader!==Mo.none&&this.rowsData.length>0){const e=document.createElement(this.rowElementTag);this.generatedHeader=e;this.generatedHeader.columnDefinitions=this.columnDefinitions;this.generatedHeader.gridTemplateColumns=this.gridTemplateColumns;this.generatedHeader.rowType=this.generateHeader===Mo.sticky?zo.stickyHeader:zo.header;if(this.firstChild!==null||this.rowsPlaceholder!==null){this.insertBefore(e,this.firstChild!==null?this.firstChild:this.rowsPlaceholder)}return}}}qo.generateColumns=e=>Object.getOwnPropertyNames(e).map(((e,t)=>({columnDataKey:e,gridColumn:`${t}`})));f([(0,s.attr)({attribute:"no-tabbing",mode:"boolean"})],qo.prototype,"noTabbing",void 0);f([(0,s.attr)({attribute:"generate-header"})],qo.prototype,"generateHeader",void 0);f([(0,s.attr)({attribute:"grid-template-columns"})],qo.prototype,"gridTemplateColumns",void 0);f([s.observable],qo.prototype,"rowsData",void 0);f([s.observable],qo.prototype,"columnDefinitions",void 0);f([s.observable],qo.prototype,"rowItemTemplate",void 0);f([s.observable],qo.prototype,"cellItemTemplate",void 0);f([s.observable],qo.prototype,"headerCellItemTemplate",void 0);f([s.observable],qo.prototype,"focusRowIndex",void 0);f([s.observable],qo.prototype,"focusColumnIndex",void 0);f([s.observable],qo.prototype,"defaultRowItemTemplate",void 0);f([s.observable],qo.prototype,"rowElementTag",void 0);f([s.observable],qo.prototype,"rowElements",void 0);const jo=s.html`
    <div
        class="title"
        part="title"
        aria-label="${e=>e.dateFormatter.getDate(`${e.month}-2-${e.year}`,{month:"long",year:"numeric"})}"
    >
        <span part="month">
            ${e=>e.dateFormatter.getMonth(e.month)}
        </span>
        <span part="year">${e=>e.dateFormatter.getYear(e.year)}</span>
    </div>
`;const _o=e=>{const t=e.tagFor(Bo);return s.html`
        <${t}
            class="week-day"
            part="week-day"
            tabindex="-1"
            grid-column="${(e,t)=>t.index+1}"
            abbr="${e=>e.abbr}"
        >
            ${e=>e.text}
        </${t}>
    `};const Ko=(e,t)=>{const i=e.tagFor(Bo);return s.html`
        <${i}
            class="${(e,i)=>i.parentContext.parent.getDayClassNames(e,t)}"
            part="day"
            tabindex="-1"
            role="gridcell"
            grid-column="${(e,t)=>t.index+1}"
            @click="${(e,t)=>t.parentContext.parent.handleDateSelect(t.event,e)}"
            @keydown="${(e,t)=>t.parentContext.parent.handleKeydown(t.event,e)}"
            aria-label="${(e,t)=>t.parentContext.parent.dateFormatter.getDate(`${e.month}-${e.day}-${e.year}`,{month:"long",day:"numeric"})}"
        >
            <div
                class="date"
                part="${e=>t===`${e.month}-${e.day}-${e.year}`?"today":"date"}"
            >
                ${(e,t)=>t.parentContext.parent.dateFormatter.getDay(e.day)}
            </div>
            <slot name="${e=>e.month}-${e=>e.day}-${e=>e.year}"></slot>
        </${i}>
    `};const Wo=(e,t)=>{const i=e.tagFor(Uo);return s.html`
        <${i}
            class="week"
            part="week"
            role="row"
            role-type="default"
            grid-template-columns="1fr 1fr 1fr 1fr 1fr 1fr 1fr"
        >
        ${(0,s.repeat)((e=>e),Ko(e,t),{positioning:true})}
        </${i}>
    `};const Go=(e,t)=>{const i=e.tagFor(qo);const n=e.tagFor(Uo);return s.html`
    <${i} class="days interact" part="days" generate-header="none">
        <${n}
            class="week-days"
            part="week-days"
            role="row"
            row-type="header"
            grid-template-columns="1fr 1fr 1fr 1fr 1fr 1fr 1fr"
        >
            ${(0,s.repeat)((e=>e.getWeekdayText()),_o(e),{positioning:true})}
        </${n}>
        ${(0,s.repeat)((e=>e.getDays()),Wo(e,t))}
    </${i}>
`};const Yo=e=>s.html`
        <div class="days" part="days">
            <div class="week-days" part="week-days">
                ${(0,s.repeat)((e=>e.getWeekdayText()),s.html`
                        <div class="week-day" part="week-day" abbr="${e=>e.abbr}">
                            ${e=>e.text}
                        </div>
                    `)}
            </div>
            ${(0,s.repeat)((e=>e.getDays()),s.html`
                    <div class="week">
                        ${(0,s.repeat)((e=>e),s.html`
                                <div
                                    class="${(t,i)=>i.parentContext.parent.getDayClassNames(t,e)}"
                                    part="day"
                                    aria-label="${(e,t)=>t.parentContext.parent.dateFormatter.getDate(`${e.month}-${e.day}-${e.year}`,{month:"long",day:"numeric"})}"
                                >
                                    <div
                                        class="date"
                                        part="${t=>e===`${t.month}-${t.day}-${t.year}`?"today":"date"}"
                                    >
                                        ${(e,t)=>t.parentContext.parent.dateFormatter.getDay(e.day)}
                                    </div>
                                    <slot
                                        name="${e=>e.month}-${e=>e.day}-${e=>e.year}"
                                    ></slot>
                                </div>
                            `)}
                    </div>
                `)}
        </div>
    `;const Xo=(e,t)=>{var i;const n=new Date;const o=`${n.getMonth()+1}-${n.getDate()}-${n.getFullYear()}`;return s.html`
        <template>
            ${l}
            ${t.title instanceof Function?t.title(e,t):(i=t.title)!==null&&i!==void 0?i:""}
            <slot></slot>
            ${(0,s.when)((e=>e.readonly),Yo(o),Go(e,o))}
            ${a}
        </template>
    `};const Qo=(e,t)=>s.html`
    <slot></slot>
`;class Zo extends Fe{}const Jo=(e,t)=>s.html`
    <template
        role="checkbox"
        aria-checked="${e=>e.checked}"
        aria-required="${e=>e.required}"
        aria-disabled="${e=>e.disabled}"
        aria-readonly="${e=>e.readOnly}"
        tabindex="${e=>e.disabled?null:0}"
        @keypress="${(e,t)=>e.keypressHandler(t.event)}"
        @click="${(e,t)=>e.clickHandler(t.event)}"
        class="${e=>e.readOnly?"readonly":""} ${e=>e.checked?"checked":""} ${e=>e.indeterminate?"indeterminate":""}"
    >
        <div part="control" class="control">
            <slot name="checked-indicator">
                ${t.checkedIndicator||""}
            </slot>
            <slot name="indeterminate-indicator">
                ${t.indeterminateIndicator||""}
            </slot>
        </div>
        <label
            part="label"
            class="${e=>e.defaultSlottedNodes&&e.defaultSlottedNodes.length?"label":"label label__hidden"}"
        >
            <slot ${(0,s.slotted)("defaultSlottedNodes")}></slot>
        </label>
    </template>
`;class er extends Fe{}class tr extends(Ro(er)){constructor(){super(...arguments);this.proxy=document.createElement("input")}}class ir extends tr{constructor(){super();this.initialValue="on";this.indeterminate=false;this.keypressHandler=e=>{if(this.readOnly){return}switch(e.key){case ui:if(this.indeterminate){this.indeterminate=false}this.checked=!this.checked;break}};this.clickHandler=e=>{if(!this.disabled&&!this.readOnly){if(this.indeterminate){this.indeterminate=false}this.checked=!this.checked}};this.proxy.setAttribute("type","checkbox")}readOnlyChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.readOnly=this.readOnly}}}f([(0,s.attr)({attribute:"readonly",mode:"boolean"})],ir.prototype,"readOnly",void 0);f([s.observable],ir.prototype,"defaultSlottedNodes",void 0);f([s.observable],ir.prototype,"indeterminate",void 0);let sr=0;function nr(e=""){return`${e}${sr++}`}function or(e,...t){return e.replace(/{(\d+)}/g,(function(e,i){if(i>=t.length){return e}const s=t[i];if(typeof s!=="number"&&!s){return""}return s}))}function rr(e,t,i=0){if(!e||!t){return false}return e.substr(i,t.length)===t}function ar(e){return!e||!e.trim()}function lr(e){let t=`${e}`.replace(new RegExp(/[-_]+/,"g")," ").replace(new RegExp(/[^\w\s]/,"g"),"").replace(/^\s+|\s+$|\s+(?=\s)/g,"").replace(new RegExp(/\s+(.)(\w*)/,"g"),((e,t,i)=>`${t.toUpperCase()+i.toLowerCase()}`)).replace(new RegExp(/\w/),(e=>e.toUpperCase()));let i=0;for(let s=0;s<t.length;s++){const e=t.charAt(s);if(e==e.toLowerCase()){i=s;break}}if(i>1){t=`${t.charAt(0).toUpperCase()}${t.slice(1,i-1).toLowerCase()}`+t.slice(i-1)}return t}function dr(e){const t=`${e.charAt(0).toLowerCase()}${e.slice(1)}`;return t.replace(/([A-Z]|[0-9])/g,(function(e,t){return`-${t.toLowerCase()}`}))}function hr(e,t){let i=e.length;while(i--){if(t(e[i],i,e)){return i}}return-1}function cr(){return!!(typeof window!=="undefined"&&window.document&&window.document.createElement)}function ur(...e){return e.every((e=>e instanceof HTMLElement))}function pr(e,t){if(!e||!t||!ur(e)){return}const i=Array.from(e.querySelectorAll(t));return i.filter((e=>e.offsetParent!==null))}function fr(e){return e===null?null:e.which||e.keyCode||e.charCode}function mr(){const e=document.querySelector('meta[property="csp-nonce"]');if(e){return e.getAttribute("content")}else{return null}}let vr;function br(){if(typeof vr==="boolean"){return vr}if(!cr()){vr=false;return vr}const e=document.createElement("style");const t=mr();if(t!==null){e.setAttribute("nonce",t)}document.head.appendChild(e);try{e.sheet.insertRule("foo:focus-visible {color:inherit}",0);vr=true}catch(i){vr=false}finally{document.head.removeChild(e)}return vr}let gr;function yr(){if(typeof gr==="boolean"){return gr}try{gr=CSS.supports("display","grid")}catch(e){gr=false}return gr}function Cr(){return canUseDOM()&&(window.matchMedia("(forced-colors: none)").matches||window.matchMedia("(forced-colors: active)").matches)}function xr(){gr=undefined;vr=undefined}const wr=null&&Cr;function $r(e){return ur(e)&&(e.getAttribute("role")==="option"||e instanceof HTMLOptionElement)}class kr extends Fe{constructor(e,t,i,s){super();this.defaultSelected=false;this.dirtySelected=false;this.selected=this.defaultSelected;this.dirtyValue=false;if(e){this.textContent=e}if(t){this.initialValue=t}if(i){this.defaultSelected=i}if(s){this.selected=s}this.proxy=new Option(`${this.textContent}`,this.initialValue,this.defaultSelected,this.selected);this.proxy.disabled=this.disabled}checkedChanged(e,t){if(typeof t==="boolean"){this.ariaChecked=t?"true":"false";return}this.ariaChecked=null}contentChanged(e,t){if(this.proxy instanceof HTMLOptionElement){this.proxy.textContent=this.textContent}this.$emit("contentchange",null,{bubbles:true})}defaultSelectedChanged(){if(!this.dirtySelected){this.selected=this.defaultSelected;if(this.proxy instanceof HTMLOptionElement){this.proxy.selected=this.defaultSelected}}}disabledChanged(e,t){this.ariaDisabled=this.disabled?"true":"false";if(this.proxy instanceof HTMLOptionElement){this.proxy.disabled=this.disabled}}selectedAttributeChanged(){this.defaultSelected=this.selectedAttribute;if(this.proxy instanceof HTMLOptionElement){this.proxy.defaultSelected=this.defaultSelected}}selectedChanged(){this.ariaSelected=this.selected?"true":"false";if(!this.dirtySelected){this.dirtySelected=true}if(this.proxy instanceof HTMLOptionElement){this.proxy.selected=this.selected}}initialValueChanged(e,t){if(!this.dirtyValue){this.value=this.initialValue;this.dirtyValue=false}}get label(){var e;return(e=this.value)!==null&&e!==void 0?e:this.text}get text(){var e,t;return(t=(e=this.textContent)===null||e===void 0?void 0:e.replace(/\s+/g," ").trim())!==null&&t!==void 0?t:""}set value(e){const t=`${e!==null&&e!==void 0?e:""}`;this._value=t;this.dirtyValue=true;if(this.proxy instanceof HTMLOptionElement){this.proxy.value=t}s.Observable.notify(this,"value")}get value(){var e;s.Observable.track(this,"value");return(e=this._value)!==null&&e!==void 0?e:this.text}get form(){return this.proxy?this.proxy.form:null}}f([s.observable],kr.prototype,"checked",void 0);f([s.observable],kr.prototype,"content",void 0);f([s.observable],kr.prototype,"defaultSelected",void 0);f([(0,s.attr)({mode:"boolean"})],kr.prototype,"disabled",void 0);f([(0,s.attr)({attribute:"selected",mode:"boolean"})],kr.prototype,"selectedAttribute",void 0);f([s.observable],kr.prototype,"selected",void 0);f([(0,s.attr)({attribute:"value",mode:"fromView"})],kr.prototype,"initialValue",void 0);class Ir{}f([s.observable],Ir.prototype,"ariaChecked",void 0);f([s.observable],Ir.prototype,"ariaPosInSet",void 0);f([s.observable],Ir.prototype,"ariaSelected",void 0);f([s.observable],Ir.prototype,"ariaSetSize",void 0);Me(Ir,$i);Me(kr,n,Ir);class Er extends Fe{constructor(){super(...arguments);this._options=[];this.selectedIndex=-1;this.selectedOptions=[];this.shouldSkipFocus=false;this.typeaheadBuffer="";this.typeaheadExpired=true;this.typeaheadTimeout=-1}get firstSelectedOption(){var e;return(e=this.selectedOptions[0])!==null&&e!==void 0?e:null}get hasSelectableOptions(){return this.options.length>0&&!this.options.every((e=>e.disabled))}get length(){var e,t;return(t=(e=this.options)===null||e===void 0?void 0:e.length)!==null&&t!==void 0?t:0}get options(){s.Observable.track(this,"options");return this._options}set options(e){this._options=e;s.Observable.notify(this,"options")}get typeAheadExpired(){return this.typeaheadExpired}set typeAheadExpired(e){this.typeaheadExpired=e}clickHandler(e){const t=e.target.closest(`option,[role=option]`);if(t&&!t.disabled){this.selectedIndex=this.options.indexOf(t);return true}}focusAndScrollOptionIntoView(e=this.firstSelectedOption){if(this.contains(document.activeElement)&&e!==null){e.focus();requestAnimationFrame((()=>{e.scrollIntoView({block:"nearest"})}))}}focusinHandler(e){if(!this.shouldSkipFocus&&e.target===e.currentTarget){this.setSelectedOptions();this.focusAndScrollOptionIntoView()}this.shouldSkipFocus=false}getTypeaheadMatches(){const e=this.typeaheadBuffer.replace(/[.*+\-?^${}()|[\]\\]/g,"\\$&");const t=new RegExp(`^${e}`,"gi");return this.options.filter((e=>e.text.trim().match(t)))}getSelectableIndex(e=this.selectedIndex,t){const i=e>t?-1:e<t?1:0;const s=e+i;let n=null;switch(i){case-1:{n=this.options.reduceRight(((e,t,i)=>!e&&!t.disabled&&i<s?t:e),n);break}case 1:{n=this.options.reduce(((e,t,i)=>!e&&!t.disabled&&i>s?t:e),n);break}}return this.options.indexOf(n)}handleChange(e,t){switch(t){case"selected":{if(Er.slottedOptionFilter(e)){this.selectedIndex=this.options.indexOf(e)}this.setSelectedOptions();break}}}handleTypeAhead(e){if(this.typeaheadTimeout){window.clearTimeout(this.typeaheadTimeout)}this.typeaheadTimeout=window.setTimeout((()=>this.typeaheadExpired=true),Er.TYPE_AHEAD_TIMEOUT_MS);if(e.length>1){return}this.typeaheadBuffer=`${this.typeaheadExpired?"":this.typeaheadBuffer}${e}`}keydownHandler(e){if(this.disabled){return true}this.shouldSkipFocus=false;const t=e.key;switch(t){case ai:{if(!e.shiftKey){e.preventDefault();this.selectFirstOption()}break}case ti:{if(!e.shiftKey){e.preventDefault();this.selectNextOption()}break}case ni:{if(!e.shiftKey){e.preventDefault();this.selectPreviousOption()}break}case li:{e.preventDefault();this.selectLastOption();break}case pi:{this.focusAndScrollOptionIntoView();return true}case oi:case ri:{return true}case ui:{if(this.typeaheadExpired){return true}}default:{if(t.length===1){this.handleTypeAhead(`${t}`)}return true}}}mousedownHandler(e){this.shouldSkipFocus=!this.contains(document.activeElement);return true}multipleChanged(e,t){this.ariaMultiSelectable=t?"true":null}selectedIndexChanged(e,t){var i;if(!this.hasSelectableOptions){this.selectedIndex=-1;return}if(((i=this.options[this.selectedIndex])===null||i===void 0?void 0:i.disabled)&&typeof e==="number"){const i=this.getSelectableIndex(e,t);const s=i>-1?i:e;this.selectedIndex=s;if(t===s){this.selectedIndexChanged(t,s)}return}this.setSelectedOptions()}selectedOptionsChanged(e,t){var i;const n=t.filter(Er.slottedOptionFilter);(i=this.options)===null||i===void 0?void 0:i.forEach((e=>{const t=s.Observable.getNotifier(e);t.unsubscribe(this,"selected");e.selected=n.includes(e);t.subscribe(this,"selected")}))}selectFirstOption(){var e,t;if(!this.disabled){this.selectedIndex=(t=(e=this.options)===null||e===void 0?void 0:e.findIndex((e=>!e.disabled)))!==null&&t!==void 0?t:-1}}selectLastOption(){if(!this.disabled){this.selectedIndex=hr(this.options,(e=>!e.disabled))}}selectNextOption(){if(!this.disabled&&this.selectedIndex<this.options.length-1){this.selectedIndex+=1}}selectPreviousOption(){if(!this.disabled&&this.selectedIndex>0){this.selectedIndex=this.selectedIndex-1}}setDefaultSelectedOption(){var e,t;this.selectedIndex=(t=(e=this.options)===null||e===void 0?void 0:e.findIndex((e=>e.defaultSelected)))!==null&&t!==void 0?t:-1}setSelectedOptions(){var e,t,i;if((e=this.options)===null||e===void 0?void 0:e.length){this.selectedOptions=[this.options[this.selectedIndex]];this.ariaActiveDescendant=(i=(t=this.firstSelectedOption)===null||t===void 0?void 0:t.id)!==null&&i!==void 0?i:"";this.focusAndScrollOptionIntoView()}}slottedOptionsChanged(e,t){this.options=t.reduce(((e,t)=>{if($r(t)){e.push(t)}return e}),[]);const i=`${this.options.length}`;this.options.forEach(((e,t)=>{if(!e.id){e.id=nr("option-")}e.ariaPosInSet=`${t+1}`;e.ariaSetSize=i}));if(this.$fastController.isConnected){this.setSelectedOptions();this.setDefaultSelectedOption()}}typeaheadBufferChanged(e,t){if(this.$fastController.isConnected){const e=this.getTypeaheadMatches();if(e.length){const t=this.options.indexOf(e[0]);if(t>-1){this.selectedIndex=t}}this.typeaheadExpired=false}}}Er.slottedOptionFilter=e=>$r(e)&&!e.hidden;Er.TYPE_AHEAD_TIMEOUT_MS=1e3;f([(0,s.attr)({mode:"boolean"})],Er.prototype,"disabled",void 0);f([s.observable],Er.prototype,"selectedIndex",void 0);f([s.observable],Er.prototype,"selectedOptions",void 0);f([s.observable],Er.prototype,"slottedOptions",void 0);f([s.observable],Er.prototype,"typeaheadBuffer",void 0);class Or{}f([s.observable],Or.prototype,"ariaActiveDescendant",void 0);f([s.observable],Or.prototype,"ariaDisabled",void 0);f([s.observable],Or.prototype,"ariaExpanded",void 0);f([s.observable],Or.prototype,"ariaMultiSelectable",void 0);Me(Or,$i);Me(Er,Or);const Tr={above:"above",below:"below"};class Rr extends Er{}class Sr extends(To(Rr)){constructor(){super(...arguments);this.proxy=document.createElement("input")}}const Dr={inline:"inline",list:"list",both:"both",none:"none"};class Ar extends Sr{constructor(){super(...arguments);this._value="";this.filteredOptions=[];this.filter="";this.forcedPosition=false;this.listboxId=nr("listbox-");this.maxHeight=0;this.open=false}formResetCallback(){super.formResetCallback();this.setDefaultSelectedOption();this.updateValue()}validate(){super.validate(this.control)}get isAutocompleteInline(){return this.autocomplete===Dr.inline||this.isAutocompleteBoth}get isAutocompleteList(){return this.autocomplete===Dr.list||this.isAutocompleteBoth}get isAutocompleteBoth(){return this.autocomplete===Dr.both}openChanged(){if(this.open){this.ariaControls=this.listboxId;this.ariaExpanded="true";this.setPositioning();this.focusAndScrollOptionIntoView();s.DOM.queueUpdate((()=>this.focus()));return}this.ariaControls="";this.ariaExpanded="false"}get options(){s.Observable.track(this,"options");return this.filteredOptions.length?this.filteredOptions:this._options}set options(e){this._options=e;s.Observable.notify(this,"options")}placeholderChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.placeholder=this.placeholder}}positionChanged(e,t){this.positionAttribute=t;this.setPositioning()}get value(){s.Observable.track(this,"value");return this._value}set value(e){var t,i,n;const o=`${this._value}`;if(this.$fastController.isConnected&&this.options){const s=this.options.findIndex((t=>t.text.toLowerCase()===e.toLowerCase()));const o=(t=this.options[this.selectedIndex])===null||t===void 0?void 0:t.text;const r=(i=this.options[s])===null||i===void 0?void 0:i.text;this.selectedIndex=o!==r?s:this.selectedIndex;e=((n=this.firstSelectedOption)===null||n===void 0?void 0:n.text)||e}if(o!==e){this._value=e;super.valueChanged(o,e);s.Observable.notify(this,"value")}}clickHandler(e){if(this.disabled){return}if(this.open){const t=e.target.closest(`option,[role=option]`);if(!t||t.disabled){return}this.selectedOptions=[t];this.control.value=t.text;this.clearSelectionRange();this.updateValue(true)}this.open=!this.open;if(this.open){this.control.focus()}return true}connectedCallback(){super.connectedCallback();this.forcedPosition=!!this.positionAttribute;if(this.value){this.initialValue=this.value}}disabledChanged(e,t){if(super.disabledChanged){super.disabledChanged(e,t)}this.ariaDisabled=this.disabled?"true":"false"}filterOptions(){if(!this.autocomplete||this.autocomplete===Dr.none){this.filter=""}const e=this.filter.toLowerCase();this.filteredOptions=this._options.filter((e=>e.text.toLowerCase().startsWith(this.filter.toLowerCase())));if(this.isAutocompleteList){if(!this.filteredOptions.length&&!e){this.filteredOptions=this._options}this._options.forEach((e=>{e.hidden=!this.filteredOptions.includes(e)}))}}focusAndScrollOptionIntoView(){if(this.contains(document.activeElement)){this.control.focus();if(this.firstSelectedOption){requestAnimationFrame((()=>{var e;(e=this.firstSelectedOption)===null||e===void 0?void 0:e.scrollIntoView({block:"nearest"})}))}}}focusoutHandler(e){this.syncValue();if(!this.open){return true}const t=e.relatedTarget;if(this.isSameNode(t)){this.focus();return}if(!this.options||!this.options.includes(t)){this.open=false}}inputHandler(e){this.filter=this.control.value;this.filterOptions();if(!this.isAutocompleteInline){this.selectedIndex=this.options.map((e=>e.text)).indexOf(this.control.value)}if(e.inputType.includes("deleteContent")||!this.filter.length){return true}if(this.isAutocompleteList&&!this.open){this.open=true}if(this.isAutocompleteInline){if(this.filteredOptions.length){this.selectedOptions=[this.filteredOptions[0]];this.selectedIndex=this.options.indexOf(this.firstSelectedOption);this.setInlineSelection()}else{this.selectedIndex=-1}}return}keydownHandler(e){const t=e.key;if(e.ctrlKey||e.shiftKey){return true}switch(t){case"Enter":{this.syncValue();if(this.isAutocompleteInline){this.filter=this.value}this.open=false;this.clearSelectionRange();break}case"Escape":{if(!this.isAutocompleteInline){this.selectedIndex=-1}if(this.open){this.open=false;break}this.value="";this.control.value="";this.filter="";this.filterOptions();break}case"Tab":{this.setInputToSelection();if(!this.open){return true}e.preventDefault();this.open=false;break}case"ArrowUp":case"ArrowDown":{this.filterOptions();if(!this.open){this.open=true;break}if(this.filteredOptions.length>0){super.keydownHandler(e)}if(this.isAutocompleteInline){this.setInlineSelection()}break}default:{return true}}}keyupHandler(e){const t=e.key;switch(t){case"ArrowLeft":case"ArrowRight":case"Backspace":case"Delete":case"Home":case"End":{this.filter=this.control.value;this.selectedIndex=-1;this.filterOptions();break}}}selectedIndexChanged(e,t){if(this.$fastController.isConnected){t=gi(-1,this.options.length-1,t);if(t!==this.selectedIndex){this.selectedIndex=t;return}super.selectedIndexChanged(e,t)}}selectPreviousOption(){if(!this.disabled&&this.selectedIndex>=0){this.selectedIndex=this.selectedIndex-1}}setDefaultSelectedOption(){if(this.$fastController.isConnected&&this.options){const e=this.options.findIndex((e=>e.getAttribute("selected")!==null||e.selected));this.selectedIndex=e;if(!this.dirtyValue&&this.firstSelectedOption){this.value=this.firstSelectedOption.text}this.setSelectedOptions()}}setInputToSelection(){if(this.firstSelectedOption){this.control.value=this.firstSelectedOption.text;this.control.focus()}}setInlineSelection(){if(this.firstSelectedOption){this.setInputToSelection();this.control.setSelectionRange(this.filter.length,this.control.value.length,"backward")}}syncValue(){var e;const t=this.selectedIndex>-1?(e=this.firstSelectedOption)===null||e===void 0?void 0:e.text:this.control.value;this.updateValue(this.value!==t)}setPositioning(){const e=this.getBoundingClientRect();const t=window.innerHeight;const i=t-e.bottom;this.position=this.forcedPosition?this.positionAttribute:e.top>i?Tr.above:Tr.below;this.positionAttribute=this.forcedPosition?this.positionAttribute:this.position;this.maxHeight=this.position===Tr.above?~~e.top:~~i}selectedOptionsChanged(e,t){if(this.$fastController.isConnected){this._options.forEach((e=>{e.selected=t.includes(e)}))}}slottedOptionsChanged(e,t){super.slottedOptionsChanged(e,t);this.updateValue()}updateValue(e){var t;if(this.$fastController.isConnected){this.value=((t=this.firstSelectedOption)===null||t===void 0?void 0:t.text)||this.control.value;this.control.value=this.value}if(e){this.$emit("change")}}clearSelectionRange(){const e=this.control.value.length;this.control.setSelectionRange(e,e)}}f([(0,s.attr)({attribute:"autocomplete",mode:"fromView"})],Ar.prototype,"autocomplete",void 0);f([s.observable],Ar.prototype,"maxHeight",void 0);f([(0,s.attr)({attribute:"open",mode:"boolean"})],Ar.prototype,"open",void 0);f([s.attr],Ar.prototype,"placeholder",void 0);f([(0,s.attr)({attribute:"position"})],Ar.prototype,"positionAttribute",void 0);f([s.observable],Ar.prototype,"position",void 0);class Fr{}f([s.observable],Fr.prototype,"ariaAutoComplete",void 0);f([s.observable],Fr.prototype,"ariaControls",void 0);Me(Fr,Or);Me(Ar,n,Fr);const Lr=(e,t)=>s.html`
    <template
        aria-disabled="${e=>e.ariaDisabled}"
        autocomplete="${e=>e.autocomplete}"
        class="${e=>e.open?"open":""} ${e=>e.disabled?"disabled":""} ${e=>e.position}"
        ?open="${e=>e.open}"
        tabindex="${e=>!e.disabled?"0":null}"
        @click="${(e,t)=>e.clickHandler(t.event)}"
        @focusout="${(e,t)=>e.focusoutHandler(t.event)}"
        @keydown="${(e,t)=>e.keydownHandler(t.event)}"
    >
        <div class="control" part="control">
            ${r(e,t)}
            <slot name="control">
                <input
                    aria-activedescendant="${e=>e.open?e.ariaActiveDescendant:null}"
                    aria-autocomplete="${e=>e.ariaAutoComplete}"
                    aria-controls="${e=>e.ariaControls}"
                    aria-disabled="${e=>e.ariaDisabled}"
                    aria-expanded="${e=>e.ariaExpanded}"
                    aria-haspopup="listbox"
                    class="selected-value"
                    part="selected-value"
                    placeholder="${e=>e.placeholder}"
                    role="combobox"
                    type="text"
                    ?disabled="${e=>e.disabled}"
                    :value="${e=>e.value}"
                    @input="${(e,t)=>e.inputHandler(t.event)}"
                    @keyup="${(e,t)=>e.keyupHandler(t.event)}"
                    ${(0,s.ref)("control")}
                />
                <div class="indicator" part="indicator" aria-hidden="true">
                    <slot name="indicator">
                        ${t.indicator||""}
                    </slot>
                </div>
            </slot>
            ${o(e,t)}
        </div>
        <div
            class="listbox"
            id="${e=>e.listboxId}"
            part="listbox"
            role="listbox"
            ?disabled="${e=>e.disabled}"
            ?hidden="${e=>!e.open}"
            ${(0,s.ref)("listbox")}
        >
            <slot
                ${(0,s.slotted)({filter:Er.slottedOptionFilter,flatten:true,property:"slottedOptions"})}
            ></slot>
        </div>
    </template>
`;function Pr(e){const t=e.tagFor(Uo);return s.html`
    <${t}
        :rowData="${e=>e}"
        :cellItemTemplate="${(e,t)=>t.parent.cellItemTemplate}"
        :headerCellItemTemplate="${(e,t)=>t.parent.headerCellItemTemplate}"
    ></${t}>
`}const Mr=(e,t)=>{const i=Pr(e);const n=e.tagFor(Uo);return s.html`
        <template
            role="grid"
            tabindex="0"
            :rowElementTag="${()=>n}"
            :defaultRowItemTemplate="${i}"
            ${(0,s.children)({property:"rowElements",filter:(0,s.elements)("[role=row]")})}
        >
            <slot></slot>
        </template>
    `};function Hr(e){const t=e.tagFor(Bo);return s.html`
    <${t}
        cell-type="${e=>e.isRowHeader?"rowheader":undefined}"
        grid-column="${(e,t)=>t.index+1}"
        :rowData="${(e,t)=>t.parent.rowData}"
        :columnDefinition="${e=>e}"
    ></${t}>
`}function zr(e){const t=e.tagFor(Bo);return s.html`
    <${t}
        cell-type="columnheader"
        grid-column="${(e,t)=>t.index+1}"
        :columnDefinition="${e=>e}"
    ></${t}>
`}const Vr=(e,t)=>{const i=Hr(e);const n=zr(e);return s.html`
        <template
            role="row"
            class="${e=>e.rowType!=="default"?e.rowType:""}"
            :defaultCellItemTemplate="${i}"
            :defaultHeaderCellItemTemplate="${n}"
            ${(0,s.children)({property:"cellElements",filter:(0,s.elements)('[role="cell"],[role="gridcell"],[role="columnheader"],[role="rowheader"]')})}
        >
            <slot ${(0,s.slotted)("slottedCellElements")}></slot>
        </template>
    `};const Nr=(e,t)=>s.html`
        <template
            tabindex="-1"
            role="${e=>!e.cellType||e.cellType==="default"?"gridcell":e.cellType}"
            class="
            ${e=>e.cellType==="columnheader"?"column-header":e.cellType==="rowheader"?"row-header":""}
            "
        >
            <slot></slot>
        </template>
    `;function Br(e){const t=e.parentElement;if(t){return t}else{const t=e.getRootNode();if(t.host instanceof HTMLElement){return t.host}}return null}function Ur(e,t){let i=t;while(i!==null){if(i===e){return true}i=Br(i)}return false}const qr=document.createElement("div");function jr(e){return e instanceof s.FASTElement}class _r{setProperty(e,t){s.DOM.queueUpdate((()=>this.target.setProperty(e,t)))}removeProperty(e){s.DOM.queueUpdate((()=>this.target.removeProperty(e)))}}class Kr extends _r{constructor(e){super();const t=new CSSStyleSheet;this.target=t.cssRules[t.insertRule(":host{}")].style;e.$fastController.addStyles(s.ElementStyles.create([t]))}}class Wr extends _r{constructor(){super();const e=new CSSStyleSheet;this.target=e.cssRules[e.insertRule(":root{}")].style;document.adoptedStyleSheets=[...document.adoptedStyleSheets,e]}}class Gr extends _r{constructor(){super();this.style=document.createElement("style");document.head.appendChild(this.style);const{sheet:e}=this.style;if(e){const t=e.insertRule(":root{}",e.cssRules.length);this.target=e.cssRules[t].style}}}class Yr{constructor(e){this.store=new Map;this.target=null;const t=e.$fastController;this.style=document.createElement("style");t.addStyles(this.style);s.Observable.getNotifier(t).subscribe(this,"isConnected");this.handleChange(t,"isConnected")}targetChanged(){if(this.target!==null){for(const[e,t]of this.store.entries()){this.target.setProperty(e,t)}}}setProperty(e,t){this.store.set(e,t);s.DOM.queueUpdate((()=>{if(this.target!==null){this.target.setProperty(e,t)}}))}removeProperty(e){this.store.delete(e);s.DOM.queueUpdate((()=>{if(this.target!==null){this.target.removeProperty(e)}}))}handleChange(e,t){const{sheet:i}=this.style;if(i){const e=i.insertRule(":host{}",i.cssRules.length);this.target=i.cssRules[e].style}else{this.target=null}}}f([s.observable],Yr.prototype,"target",void 0);class Xr{constructor(e){this.target=e.style}setProperty(e,t){s.DOM.queueUpdate((()=>this.target.setProperty(e,t)))}removeProperty(e){s.DOM.queueUpdate((()=>this.target.removeProperty(e)))}}class Qr{setProperty(e,t){Qr.properties[e]=t;for(const i of Qr.roots.values()){ea.getOrCreate(Qr.normalizeRoot(i)).setProperty(e,t)}}removeProperty(e){delete Qr.properties[e];for(const t of Qr.roots.values()){ea.getOrCreate(Qr.normalizeRoot(t)).removeProperty(e)}}static registerRoot(e){const{roots:t}=Qr;if(!t.has(e)){t.add(e);const i=ea.getOrCreate(this.normalizeRoot(e));for(const e in Qr.properties){i.setProperty(e,Qr.properties[e])}}}static unregisterRoot(e){const{roots:t}=Qr;if(t.has(e)){t.delete(e);const i=ea.getOrCreate(Qr.normalizeRoot(e));for(const e in Qr.properties){i.removeProperty(e)}}}static normalizeRoot(e){return e===qr?document:e}}Qr.roots=new Set;Qr.properties={};const Zr=new WeakMap;const Jr=s.DOM.supportsAdoptedStyleSheets?Kr:Yr;const ea=Object.freeze({getOrCreate(e){if(Zr.has(e)){return Zr.get(e)}let t;if(e===qr){t=new Qr}else if(e instanceof Document){t=s.DOM.supportsAdoptedStyleSheets?new Wr:new Gr}else if(jr(e)){t=new Jr(e)}else{t=new Xr(e)}Zr.set(e,t);return t}});class ta extends s.CSSDirective{constructor(e){super();this.subscribers=new WeakMap;this._appliedTo=new Set;this.name=e.name;if(e.cssCustomPropertyName!==null){this.cssCustomProperty=`--${e.cssCustomPropertyName}`;this.cssVar=`var(${this.cssCustomProperty})`}this.id=ta.uniqueId();ta.tokensById.set(this.id,this)}get appliedTo(){return[...this._appliedTo]}static from(e){return new ta({name:typeof e==="string"?e:e.name,cssCustomPropertyName:typeof e==="string"?e:e.cssCustomPropertyName===void 0?e.name:e.cssCustomPropertyName})}static isCSSDesignToken(e){return typeof e.cssCustomProperty==="string"}static isDerivedDesignTokenValue(e){return typeof e==="function"}static getTokenById(e){return ta.tokensById.get(e)}getOrCreateSubscriberSet(e=this){return this.subscribers.get(e)||this.subscribers.set(e,new Set)&&this.subscribers.get(e)}createCSS(){return this.cssVar||""}getValueFor(e){const t=aa.getOrCreate(e).get(this);if(t!==undefined){return t}throw new Error(`Value could not be retrieved for token named "${this.name}". Ensure the value is set for ${e} or an ancestor of ${e}.`)}setValueFor(e,t){this._appliedTo.add(e);if(t instanceof ta){t=this.alias(t)}aa.getOrCreate(e).set(this,t);return this}deleteValueFor(e){this._appliedTo.delete(e);if(aa.existsFor(e)){aa.getOrCreate(e).delete(this)}return this}withDefault(e){this.setValueFor(qr,e);return this}subscribe(e,t){const i=this.getOrCreateSubscriberSet(t);if(t&&!aa.existsFor(t)){aa.getOrCreate(t)}if(!i.has(e)){i.add(e)}}unsubscribe(e,t){const i=this.subscribers.get(t||this);if(i&&i.has(e)){i.delete(e)}}notify(e){const t=Object.freeze({token:this,target:e});if(this.subscribers.has(this)){this.subscribers.get(this).forEach((e=>e.handleChange(t)))}if(this.subscribers.has(e)){this.subscribers.get(e).forEach((e=>e.handleChange(t)))}}alias(e){return t=>e.getValueFor(t)}}ta.uniqueId=(()=>{let e=0;return()=>{e++;return e.toString(16)}})();ta.tokensById=new Map;class ia{startReflection(e,t){e.subscribe(this,t);this.handleChange({token:e,target:t})}stopReflection(e,t){e.unsubscribe(this,t);this.remove(e,t)}handleChange(e){const{token:t,target:i}=e;this.add(t,i)}add(e,t){ea.getOrCreate(t).setProperty(e.cssCustomProperty,this.resolveCSSValue(aa.getOrCreate(t).get(e)))}remove(e,t){ea.getOrCreate(t).removeProperty(e.cssCustomProperty)}resolveCSSValue(e){return e&&typeof e.createCSS==="function"?e.createCSS():e}}class sa{constructor(e,t,i){this.source=e;this.token=t;this.node=i;this.dependencies=new Set;this.observer=s.Observable.binding(e,this,false);this.observer.handleChange=this.observer.call;this.handleChange()}disconnect(){this.observer.disconnect()}handleChange(){this.node.store.set(this.token,this.observer.observe(this.node.target,s.defaultExecutionContext))}}class na{constructor(){this.values=new Map}set(e,t){if(this.values.get(e)!==t){this.values.set(e,t);s.Observable.getNotifier(this).notify(e.id)}}get(e){s.Observable.track(this,e.id);return this.values.get(e)}delete(e){this.values.delete(e)}all(){return this.values.entries()}}const oa=new WeakMap;const ra=new WeakMap;class aa{constructor(e){this.target=e;this.store=new na;this.children=[];this.assignedValues=new Map;this.reflecting=new Set;this.bindingObservers=new Map;this.tokenValueChangeHandler={handleChange:(e,t)=>{const i=ta.getTokenById(t);if(i){i.notify(this.target);if(ta.isCSSDesignToken(i)){const t=this.parent;const s=this.isReflecting(i);if(t){const n=t.get(i);const o=e.get(i);if(n!==o&&!s){this.reflectToCSS(i)}else if(n===o&&s){this.stopReflectToCSS(i)}}else if(!s){this.reflectToCSS(i)}}}}};oa.set(e,this);s.Observable.getNotifier(this.store).subscribe(this.tokenValueChangeHandler);if(e instanceof s.FASTElement){e.$fastController.addBehaviors([this])}else if(e.isConnected){this.bind()}}static getOrCreate(e){return oa.get(e)||new aa(e)}static existsFor(e){return oa.has(e)}static findParent(e){if(!(qr===e.target)){let t=Br(e.target);while(t!==null){if(oa.has(t)){return oa.get(t)}t=Br(t)}return aa.getOrCreate(qr)}return null}static findClosestAssignedNode(e,t){let i=t;do{if(i.has(e)){return i}i=i.parent?i.parent:i.target!==qr?aa.getOrCreate(qr):null}while(i!==null);return null}get parent(){return ra.get(this)||null}has(e){return this.assignedValues.has(e)}get(e){const t=this.store.get(e);if(t!==undefined){return t}const i=this.getRaw(e);if(i!==undefined){this.hydrate(e,i);return this.get(e)}}getRaw(e){var t;if(this.assignedValues.has(e)){return this.assignedValues.get(e)}return(t=aa.findClosestAssignedNode(e,this))===null||t===void 0?void 0:t.getRaw(e)}set(e,t){if(ta.isDerivedDesignTokenValue(this.assignedValues.get(e))){this.tearDownBindingObserver(e)}this.assignedValues.set(e,t);if(ta.isDerivedDesignTokenValue(t)){this.setupBindingObserver(e,t)}else{this.store.set(e,t)}}delete(e){this.assignedValues.delete(e);this.tearDownBindingObserver(e);const t=this.getRaw(e);if(t){this.hydrate(e,t)}else{this.store.delete(e)}}bind(){const e=aa.findParent(this);if(e){e.appendChild(this)}for(const t of this.assignedValues.keys()){t.notify(this.target)}}unbind(){if(this.parent){const e=ra.get(this);e.removeChild(this)}}appendChild(e){if(e.parent){ra.get(e).removeChild(e)}const t=this.children.filter((t=>e.contains(t)));ra.set(e,this);this.children.push(e);t.forEach((t=>e.appendChild(t)));s.Observable.getNotifier(this.store).subscribe(e);for(const[i,s]of this.store.all()){e.hydrate(i,this.bindingObservers.has(i)?this.getRaw(i):s)}}removeChild(e){const t=this.children.indexOf(e);if(t!==-1){this.children.splice(t,1)}s.Observable.getNotifier(this.store).unsubscribe(e);return e.parent===this?ra.delete(e):false}contains(e){return Ur(this.target,e.target)}reflectToCSS(e){if(!this.isReflecting(e)){this.reflecting.add(e);aa.cssCustomPropertyReflector.startReflection(e,this.target)}}stopReflectToCSS(e){if(this.isReflecting(e)){this.reflecting.delete(e);aa.cssCustomPropertyReflector.stopReflection(e,this.target)}}isReflecting(e){return this.reflecting.has(e)}handleChange(e,t){const i=ta.getTokenById(t);if(!i){return}this.hydrate(i,this.getRaw(i))}hydrate(e,t){if(!this.has(e)){const i=this.bindingObservers.get(e);if(ta.isDerivedDesignTokenValue(t)){if(i){if(i.source!==t){this.tearDownBindingObserver(e);this.setupBindingObserver(e,t)}}else{this.setupBindingObserver(e,t)}}else{if(i){this.tearDownBindingObserver(e)}this.store.set(e,t)}}}setupBindingObserver(e,t){const i=new sa(t,e,this);this.bindingObservers.set(e,i);return i}tearDownBindingObserver(e){if(this.bindingObservers.has(e)){this.bindingObservers.get(e).disconnect();this.bindingObservers.delete(e);return true}return false}}aa.cssCustomPropertyReflector=new ia;f([s.observable],aa.prototype,"children",void 0);function la(e){return ta.from(e)}const da=Object.freeze({create:la,notifyConnection(e){if(!e.isConnected||!aa.existsFor(e)){return false}aa.getOrCreate(e).bind();return true},notifyDisconnection(e){if(e.isConnected||!aa.existsFor(e)){return false}aa.getOrCreate(e).unbind();return true},registerRoot(e=qr){Qr.registerRoot(e)},unregisterRoot(e=qr){Qr.unregisterRoot(e)}});const ha=Object.freeze({definitionCallbackOnly:null,ignoreDuplicate:Symbol()});const ca=new Map;const ua=new Map;let pa=null;const fa=U.createInterface((e=>e.cachedCallback((e=>{if(pa===null){pa=new ba(null,e)}return pa}))));const ma=Object.freeze({tagFor(e){return ua.get(e)},responsibleFor(e){const t=e.$$designSystem$$;if(t){return t}const i=U.findResponsibleContainer(e);return i.get(fa)},getOrCreate(e){if(!e){if(pa===null){pa=U.getOrCreateDOMContainer().get(fa)}return pa}const t=e.$$designSystem$$;if(t){return t}const i=U.getOrCreateDOMContainer(e);if(i.has(fa,false)){return i.get(fa)}else{const t=new ba(e,i);i.register(xe.instance(fa,t));return t}}});function va(e,t,i){if(typeof e==="string"){return{name:e,type:t,callback:i}}else{return e}}class ba{constructor(e,t){this.owner=e;this.container=t;this.designTokensInitialized=false;this.prefix="fast";this.shadowRootMode=undefined;this.disambiguate=()=>ha.definitionCallbackOnly;if(e!==null){e.$$designSystem$$=this}}withPrefix(e){this.prefix=e;return this}withShadowRootMode(e){this.shadowRootMode=e;return this}withElementDisambiguation(e){this.disambiguate=e;return this}withDesignTokenRoot(e){this.designTokenRoot=e;return this}register(...e){const t=this.container;const i=[];const s=this.disambiguate;const n=this.shadowRootMode;const o={elementPrefix:this.prefix,tryDefineElement(e,o,r){const a=va(e,o,r);const{name:l,callback:d,baseClass:h}=a;let{type:c}=a;let u=l;let p=ca.get(u);let f=true;while(p){const e=s(u,c,p);switch(e){case ha.ignoreDuplicate:return;case ha.definitionCallbackOnly:f=false;p=void 0;break;default:u=e;p=ca.get(u);break}}if(f){if(ua.has(c)||c===Fe){c=class extends c{}}ca.set(u,c);ua.set(c,u);if(h){ua.set(h,u)}}i.push(new ga(t,u,c,n,d,f))}};if(!this.designTokensInitialized){this.designTokensInitialized=true;if(this.designTokenRoot!==null){da.registerRoot(this.designTokenRoot)}}t.registerWithContext(o,...e);for(const r of i){r.callback(r);if(r.willDefine&&r.definition!==null){r.definition.define()}}return this}}class ga{constructor(e,t,i,s,n,o){this.container=e;this.name=t;this.type=i;this.shadowRootMode=s;this.callback=n;this.willDefine=o;this.definition=null}definePresentation(e){De.define(this.name,e,this.container)}defineElement(e){this.definition=new s.FASTElementDefinition(this.type,Object.assign(Object.assign({},e),{name:this.name}))}tagFor(e){return ma.tagFor(e)}}const ya=(e,t)=>s.html`
    <div class="positioning-region" part="positioning-region">
        ${(0,s.when)((e=>e.modal),s.html`
                <div
                    class="overlay"
                    part="overlay"
                    role="presentation"
                    @click="${e=>e.dismiss()}"
                ></div>
            `)}
        <div
            role="dialog"
            tabindex="-1"
            class="control"
            part="control"
            aria-modal="${e=>e.modal}"
            aria-describedby="${e=>e.ariaDescribedby}"
            aria-labelledby="${e=>e.ariaLabelledby}"
            aria-label="${e=>e.ariaLabel}"
            ${(0,s.ref)("dialog")}
        >
            <slot></slot>
        </div>
    </div>
`;var Ca=["input","select","textarea","a[href]","button","[tabindex]:not(slot)","audio[controls]","video[controls]",'[contenteditable]:not([contenteditable="false"])',"details>summary:first-of-type","details"];var xa=Ca.join(",");var wa=typeof Element==="undefined";var $a=wa?function(){}:Element.prototype.matches||Element.prototype.msMatchesSelector||Element.prototype.webkitMatchesSelector;var ka=!wa&&Element.prototype.getRootNode?function(e){return e.getRootNode()}:function(e){return e.ownerDocument};var Ia=function e(t,i,s){var n=Array.prototype.slice.apply(t.querySelectorAll(xa));if(i&&$a.call(t,xa)){n.unshift(t)}n=n.filter(s);return n};var Ea=function e(t,i,s){var n=[];var o=Array.from(t);while(o.length){var r=o.shift();if(r.tagName==="SLOT"){var a=r.assignedElements();var l=a.length?a:r.children;var d=e(l,true,s);if(s.flatten){n.push.apply(n,d)}else{n.push({scope:r,candidates:d})}}else{var h=$a.call(r,xa);if(h&&s.filter(r)&&(i||!t.includes(r))){n.push(r)}var c=r.shadowRoot||typeof s.getShadowRoot==="function"&&s.getShadowRoot(r);var u=!s.shadowRootFilter||s.shadowRootFilter(r);if(c&&u){var p=e(c===true?r.children:c.children,true,s);if(s.flatten){n.push.apply(n,p)}else{n.push({scope:r,candidates:p})}}else{o.unshift.apply(o,r.children)}}}return n};var Oa=function e(t,i){if(t.tabIndex<0){if((i||/^(AUDIO|VIDEO|DETAILS)$/.test(t.tagName)||t.isContentEditable)&&isNaN(parseInt(t.getAttribute("tabindex"),10))){return 0}}return t.tabIndex};var Ta=function e(t,i){return t.tabIndex===i.tabIndex?t.documentOrder-i.documentOrder:t.tabIndex-i.tabIndex};var Ra=function e(t){return t.tagName==="INPUT"};var Sa=function e(t){return Ra(t)&&t.type==="hidden"};var Da=function e(t){var i=t.tagName==="DETAILS"&&Array.prototype.slice.apply(t.children).some((function(e){return e.tagName==="SUMMARY"}));return i};var Aa=function e(t,i){for(var s=0;s<t.length;s++){if(t[s].checked&&t[s].form===i){return t[s]}}};var Fa=function e(t){if(!t.name){return true}var i=t.form||ka(t);var s=function e(t){return i.querySelectorAll('input[type="radio"][name="'+t+'"]')};var n;if(typeof window!=="undefined"&&typeof window.CSS!=="undefined"&&typeof window.CSS.escape==="function"){n=s(window.CSS.escape(t.name))}else{try{n=s(t.name)}catch(r){console.error("Looks like you have a radio button with a name attribute containing invalid CSS selector characters and need the CSS.escape polyfill: %s",r.message);return false}}var o=Aa(n,t.form);return!o||o===t};var La=function e(t){return Ra(t)&&t.type==="radio"};var Pa=function e(t){return La(t)&&!Fa(t)};var Ma=function e(t){var i=t.getBoundingClientRect(),s=i.width,n=i.height;return s===0&&n===0};var Ha=function e(t,i){var s=i.displayCheck,n=i.getShadowRoot;if(getComputedStyle(t).visibility==="hidden"){return true}var o=$a.call(t,"details>summary:first-of-type");var r=o?t.parentElement:t;if($a.call(r,"details:not([open]) *")){return true}var a=ka(t).host;var l=(a===null||a===void 0?void 0:a.ownerDocument.contains(a))||t.ownerDocument.contains(t);if(!s||s==="full"){if(typeof n==="function"){var d=t;while(t){var h=t.parentElement;var c=ka(t);if(h&&!h.shadowRoot&&n(h)===true){return Ma(t)}else if(t.assignedSlot){t=t.assignedSlot}else if(!h&&c!==t.ownerDocument){t=c.host}else{t=h}}t=d}if(l){return!t.getClientRects().length}}else if(s==="non-zero-area"){return Ma(t)}return false};var za=function e(t){if(/^(INPUT|BUTTON|SELECT|TEXTAREA)$/.test(t.tagName)){var i=t.parentElement;while(i){if(i.tagName==="FIELDSET"&&i.disabled){for(var s=0;s<i.children.length;s++){var n=i.children.item(s);if(n.tagName==="LEGEND"){return $a.call(i,"fieldset[disabled] *")?true:!n.contains(t)}}return true}i=i.parentElement}}return false};var Va=function e(t,i){if(i.disabled||Sa(i)||Ha(i,t)||Da(i)||za(i)){return false}return true};var Na=function e(t,i){if(Pa(i)||Oa(i)<0||!Va(t,i)){return false}return true};var Ba=function e(t){var i=parseInt(t.getAttribute("tabindex"),10);if(isNaN(i)||i>=0){return true}return false};var Ua=function e(t){var i=[];var s=[];t.forEach((function(t,n){var o=!!t.scope;var r=o?t.scope:t;var a=Oa(r,o);var l=o?e(t.candidates):r;if(a===0){o?i.push.apply(i,l):i.push(r)}else{s.push({documentOrder:n,tabIndex:a,item:t,isScope:o,content:l})}}));return s.sort(Ta).reduce((function(e,t){t.isScope?e.push.apply(e,t.content):e.push(t.content);return e}),[]).concat(i)};var qa=function e(t,i){i=i||{};var s;if(i.getShadowRoot){s=Ea([t],i.includeContainer,{filter:Na.bind(null,i),flatten:false,getShadowRoot:i.getShadowRoot,shadowRootFilter:Ba})}else{s=Ia(t,i.includeContainer,Na.bind(null,i))}return Ua(s)};var ja=function e(t,i){i=i||{};var s;if(i.getShadowRoot){s=Ea([t],i.includeContainer,{filter:Va.bind(null,i),flatten:true,getShadowRoot:i.getShadowRoot})}else{s=Ia(t,i.includeContainer,Va.bind(null,i))}return s};var _a=function e(t,i){i=i||{};if(!t){throw new Error("No node provided")}if($a.call(t,xa)===false){return false}return Na(i,t)};var Ka=Ca.concat("iframe").join(",");var Wa=function e(t,i){i=i||{};if(!t){throw new Error("No node provided")}if($a.call(t,Ka)===false){return false}return Va(i,t)};class Ga extends Fe{constructor(){super(...arguments);this.modal=true;this.hidden=false;this.trapFocus=true;this.trapFocusChanged=()=>{if(this.$fastController.isConnected){this.updateTrapFocus()}};this.isTrappingFocus=false;this.handleDocumentKeydown=e=>{if(!e.defaultPrevented&&!this.hidden){switch(e.key){case ri:this.dismiss();e.preventDefault();break;case pi:this.handleTabKeyDown(e);break}}};this.handleDocumentFocus=e=>{if(!e.defaultPrevented&&this.shouldForceFocus(e.target)){this.focusFirstElement();e.preventDefault()}};this.handleTabKeyDown=e=>{if(!this.trapFocus||this.hidden){return}const t=this.getTabQueueBounds();if(t.length===0){return}if(t.length===1){t[0].focus();e.preventDefault();return}if(e.shiftKey&&e.target===t[0]){t[t.length-1].focus();e.preventDefault()}else if(!e.shiftKey&&e.target===t[t.length-1]){t[0].focus();e.preventDefault()}return};this.getTabQueueBounds=()=>{const e=[];return Ga.reduceTabbableItems(e,this)};this.focusFirstElement=()=>{const e=this.getTabQueueBounds();if(e.length>0){e[0].focus()}else{if(this.dialog instanceof HTMLElement){this.dialog.focus()}}};this.shouldForceFocus=e=>this.isTrappingFocus&&!this.contains(e);this.shouldTrapFocus=()=>this.trapFocus&&!this.hidden;this.updateTrapFocus=e=>{const t=e===undefined?this.shouldTrapFocus():e;if(t&&!this.isTrappingFocus){this.isTrappingFocus=true;document.addEventListener("focusin",this.handleDocumentFocus);s.DOM.queueUpdate((()=>{if(this.shouldForceFocus(document.activeElement)){this.focusFirstElement()}}))}else if(!t&&this.isTrappingFocus){this.isTrappingFocus=false;document.removeEventListener("focusin",this.handleDocumentFocus)}}}dismiss(){this.$emit("dismiss");this.$emit("cancel")}show(){this.hidden=false}hide(){this.hidden=true;this.$emit("close")}connectedCallback(){super.connectedCallback();document.addEventListener("keydown",this.handleDocumentKeydown);this.notifier=s.Observable.getNotifier(this);this.notifier.subscribe(this,"hidden");this.updateTrapFocus()}disconnectedCallback(){super.disconnectedCallback();document.removeEventListener("keydown",this.handleDocumentKeydown);this.updateTrapFocus(false);this.notifier.unsubscribe(this,"hidden")}handleChange(e,t){switch(t){case"hidden":this.updateTrapFocus();break;default:break}}static reduceTabbableItems(e,t){if(t.getAttribute("tabindex")==="-1"){return e}if(_a(t)||Ga.isFocusableFastElement(t)&&Ga.hasTabbableShadow(t)){e.push(t);return e}if(t.childElementCount){return e.concat(Array.from(t.children).reduce(Ga.reduceTabbableItems,[]))}return e}static isFocusableFastElement(e){var t,i;return!!((i=(t=e.$fastController)===null||t===void 0?void 0:t.definition.shadowOptions)===null||i===void 0?void 0:i.delegatesFocus)}static hasTabbableShadow(e){var t,i;return Array.from((i=(t=e.shadowRoot)===null||t===void 0?void 0:t.querySelectorAll("*"))!==null&&i!==void 0?i:[]).some((e=>_a(e)))}}f([(0,s.attr)({mode:"boolean"})],Ga.prototype,"modal",void 0);f([(0,s.attr)({mode:"boolean"})],Ga.prototype,"hidden",void 0);f([(0,s.attr)({attribute:"trap-focus",mode:"boolean"})],Ga.prototype,"trapFocus",void 0);f([(0,s.attr)({attribute:"aria-describedby"})],Ga.prototype,"ariaDescribedby",void 0);f([(0,s.attr)({attribute:"aria-labelledby"})],Ga.prototype,"ariaLabelledby",void 0);f([(0,s.attr)({attribute:"aria-label"})],Ga.prototype,"ariaLabel",void 0);const Ya=new MutationObserver((e=>{for(const t of e){Xa.getOrCreateFor(t.target).notify(t.attributeName)}}));class Xa extends s.SubscriberSet{constructor(e){super(e);this.watchedAttributes=new Set;Xa.subscriberCache.set(e,this)}subscribe(e){super.subscribe(e);if(!this.watchedAttributes.has(e.attributes)){this.watchedAttributes.add(e.attributes);this.observe()}}unsubscribe(e){super.unsubscribe(e);if(this.watchedAttributes.has(e.attributes)){this.watchedAttributes.delete(e.attributes);this.observe()}}static getOrCreateFor(e){return this.subscriberCache.get(e)||new Xa(e)}observe(){const e=[];for(const t of this.watchedAttributes.values()){for(let i=0;i<t.length;i++){e.push(t[i])}}Ya.observe(this.source,{attributeFilter:e})}}Xa.subscriberCache=new WeakMap;class Qa{constructor(e,t){this.target=e;this.attributes=Object.freeze(t)}bind(e){Xa.getOrCreateFor(e).subscribe(this);if(e.hasAttributes()){for(let t=0;t<e.attributes.length;t++){this.handleChange(e,e.attributes[t].name)}}}unbind(e){Xa.getOrCreateFor(e).unsubscribe(this)}handleChange(e,t){if(this.attributes.includes(t)){s.DOM.setAttribute(this.target,t,e.getAttribute(t))}}}function Za(...e){return new s.AttachedBehaviorHTMLDirective("fast-reflect-attr",Qa,e)}const Ja=(e,t)=>s.html`
    <details class="disclosure" ${(0,s.ref)("details")}>
        <summary
            class="invoker"
            role="button"
            aria-controls="disclosure-content"
            aria-expanded="${e=>e.expanded}"
        >
            <slot name="start"></slot>
            <slot name="title">${e=>e.title}</slot>
            <slot name="end"></slot>
        </summary>
        <div id="disclosure-content"><slot></slot></div>
    </details>
`;class el extends Fe{connectedCallback(){super.connectedCallback();this.setup()}disconnectedCallback(){super.disconnectedCallback();this.details.removeEventListener("toggle",this.onToggle)}show(){this.details.open=true}hide(){this.details.open=false}toggle(){this.details.open=!this.details.open}setup(){this.onToggle=this.onToggle.bind(this);this.details.addEventListener("toggle",this.onToggle);if(this.expanded){this.show()}}onToggle(){this.expanded=this.details.open;this.$emit("toggle")}}f([(0,s.attr)({mode:"boolean"})],el.prototype,"expanded",void 0);f([s.attr],el.prototype,"title",void 0);const tl=(e,t)=>s.html`
    <template role="${e=>e.role}" aria-orientation="${e=>e.orientation}"></template>
`;var il=i(62899);const sl={separator:"separator",presentation:"presentation"};class nl extends Fe{constructor(){super(...arguments);this.role=sl.separator;this.orientation=il.i.horizontal}}f([s.attr],nl.prototype,"role",void 0);f([s.attr],nl.prototype,"orientation",void 0);const ol={next:"next",previous:"previous"};const rl=(e,t)=>s.html`
    <template
        role="button"
        aria-disabled="${e=>e.disabled?true:void 0}"
        tabindex="${e=>e.hiddenFromAT?-1:0}"
        class="${e=>e.direction} ${e=>e.disabled?"disabled":""}"
        @keyup="${(e,t)=>e.keyupHandler(t.event)}"
    >
        ${(0,s.when)((e=>e.direction===ol.next),s.html`
                <span part="next" class="next">
                    <slot name="next">
                        ${t.next||""}
                    </slot>
                </span>
            `)}
        ${(0,s.when)((e=>e.direction===ol.previous),s.html`
                <span part="previous" class="previous">
                    <slot name="previous">
                        ${t.previous||""}
                    </slot>
                </span>
            `)}
    </template>
`;class al extends Fe{constructor(){super(...arguments);this.hiddenFromAT=true;this.direction=ol.next}keyupHandler(e){if(!this.hiddenFromAT){const t=e.key;if(t==="Enter"||t==="Space"){this.$emit("click",e)}if(t==="Escape"){this.blur()}}}}f([(0,s.attr)({mode:"boolean"})],al.prototype,"disabled",void 0);f([(0,s.attr)({attribute:"aria-hidden",converter:s.booleanConverter})],al.prototype,"hiddenFromAT",void 0);f([s.attr],al.prototype,"direction",void 0);const ll=(e,t)=>s.html`
    <template
        aria-checked="${e=>e.ariaChecked}"
        aria-disabled="${e=>e.ariaDisabled}"
        aria-posinset="${e=>e.ariaPosInSet}"
        aria-selected="${e=>e.ariaSelected}"
        aria-setsize="${e=>e.ariaSetSize}"
        class="${e=>[e.checked&&"checked",e.selected&&"selected",e.disabled&&"disabled"].filter(Boolean).join(" ")}"
        role="option"
    >
        ${r(e,t)}
        <span class="content" part="content">
            <slot ${(0,s.slotted)("content")}></slot>
        </span>
        ${o(e,t)}
    </template>
`;class dl extends Er{constructor(){super(...arguments);this.activeIndex=-1;this.rangeStartIndex=-1}get activeOption(){return this.options[this.activeIndex]}get checkedOptions(){var e;return(e=this.options)===null||e===void 0?void 0:e.filter((e=>e.checked))}get firstSelectedOptionIndex(){return this.options.indexOf(this.firstSelectedOption)}activeIndexChanged(e,t){var i,s;this.ariaActiveDescendant=(s=(i=this.options[t])===null||i===void 0?void 0:i.id)!==null&&s!==void 0?s:"";this.focusAndScrollOptionIntoView()}checkActiveIndex(){if(!this.multiple){return}const e=this.activeOption;if(e){e.checked=true}}checkFirstOption(e=false){if(e){if(this.rangeStartIndex===-1){this.rangeStartIndex=this.activeIndex+1}this.options.forEach(((e,t)=>{e.checked=yi(t,this.rangeStartIndex)}))}else{this.uncheckAllOptions()}this.activeIndex=0;this.checkActiveIndex()}checkLastOption(e=false){if(e){if(this.rangeStartIndex===-1){this.rangeStartIndex=this.activeIndex}this.options.forEach(((e,t)=>{e.checked=yi(t,this.rangeStartIndex,this.options.length)}))}else{this.uncheckAllOptions()}this.activeIndex=this.options.length-1;this.checkActiveIndex()}connectedCallback(){super.connectedCallback();this.addEventListener("focusout",this.focusoutHandler)}disconnectedCallback(){this.removeEventListener("focusout",this.focusoutHandler);super.disconnectedCallback()}checkNextOption(e=false){if(e){if(this.rangeStartIndex===-1){this.rangeStartIndex=this.activeIndex}this.options.forEach(((e,t)=>{e.checked=yi(t,this.rangeStartIndex,this.activeIndex+1)}))}else{this.uncheckAllOptions()}this.activeIndex+=this.activeIndex<this.options.length-1?1:0;this.checkActiveIndex()}checkPreviousOption(e=false){if(e){if(this.rangeStartIndex===-1){this.rangeStartIndex=this.activeIndex}if(this.checkedOptions.length===1){this.rangeStartIndex+=1}this.options.forEach(((e,t)=>{e.checked=yi(t,this.activeIndex,this.rangeStartIndex)}))}else{this.uncheckAllOptions()}this.activeIndex-=this.activeIndex>0?1:0;this.checkActiveIndex()}clickHandler(e){var t;if(!this.multiple){return super.clickHandler(e)}const i=(t=e.target)===null||t===void 0?void 0:t.closest(`[role=option]`);if(!i||i.disabled){return}this.uncheckAllOptions();this.activeIndex=this.options.indexOf(i);this.checkActiveIndex();this.toggleSelectedForAllCheckedOptions();return true}focusAndScrollOptionIntoView(){super.focusAndScrollOptionIntoView(this.activeOption)}focusinHandler(e){if(!this.multiple){return super.focusinHandler(e)}if(!this.shouldSkipFocus&&e.target===e.currentTarget){this.uncheckAllOptions();if(this.activeIndex===-1){this.activeIndex=this.firstSelectedOptionIndex!==-1?this.firstSelectedOptionIndex:0}this.checkActiveIndex();this.setSelectedOptions();this.focusAndScrollOptionIntoView()}this.shouldSkipFocus=false}focusoutHandler(e){if(this.multiple){this.uncheckAllOptions()}}keydownHandler(e){if(!this.multiple){return super.keydownHandler(e)}if(this.disabled){return true}const{key:t,shiftKey:i}=e;this.shouldSkipFocus=false;switch(t){case ai:{this.checkFirstOption(i);return}case ti:{this.checkNextOption(i);return}case ni:{this.checkPreviousOption(i);return}case li:{this.checkLastOption(i);return}case pi:{this.focusAndScrollOptionIntoView();return true}case ri:{this.uncheckAllOptions();this.checkActiveIndex();return true}case ui:{e.preventDefault();if(this.typeAheadExpired){this.toggleSelectedForAllCheckedOptions();return}}default:{if(t.length===1){this.handleTypeAhead(`${t}`)}return true}}}mousedownHandler(e){if(e.offsetX>=0&&e.offsetX<=this.scrollWidth){return super.mousedownHandler(e)}}multipleChanged(e,t){var i;this.ariaMultiSelectable=t?"true":null;(i=this.options)===null||i===void 0?void 0:i.forEach((e=>{e.checked=t?false:undefined}));this.setSelectedOptions()}setSelectedOptions(){if(!this.multiple){super.setSelectedOptions();return}if(this.$fastController.isConnected&&this.options){this.selectedOptions=this.options.filter((e=>e.selected));this.focusAndScrollOptionIntoView()}}sizeChanged(e,t){var i;const n=Math.max(0,parseInt((i=t===null||t===void 0?void 0:t.toFixed())!==null&&i!==void 0?i:"",10));if(n!==t){s.DOM.queueUpdate((()=>{this.size=n}))}}toggleSelectedForAllCheckedOptions(){const e=this.checkedOptions.filter((e=>!e.disabled));const t=!e.every((e=>e.selected));e.forEach((e=>e.selected=t));this.selectedIndex=this.options.indexOf(e[e.length-1]);this.setSelectedOptions()}typeaheadBufferChanged(e,t){if(!this.multiple){super.typeaheadBufferChanged(e,t);return}if(this.$fastController.isConnected){const e=this.getTypeaheadMatches();const t=this.options.indexOf(e[0]);if(t>-1){this.activeIndex=t;this.uncheckAllOptions();this.checkActiveIndex()}this.typeAheadExpired=false}}uncheckAllOptions(e=false){this.options.forEach((e=>e.checked=this.multiple?false:undefined));if(!e){this.rangeStartIndex=-1}}}f([s.observable],dl.prototype,"activeIndex",void 0);f([(0,s.attr)({mode:"boolean"})],dl.prototype,"multiple",void 0);f([(0,s.attr)({converter:s.nullableNumberConverter})],dl.prototype,"size",void 0);const hl=(e,t)=>s.html`
    <template
        aria-activedescendant="${e=>e.ariaActiveDescendant}"
        aria-multiselectable="${e=>e.ariaMultiSelectable}"
        class="listbox"
        role="listbox"
        tabindex="${e=>!e.disabled?"0":null}"
        @click="${(e,t)=>e.clickHandler(t.event)}"
        @focusin="${(e,t)=>e.focusinHandler(t.event)}"
        @keydown="${(e,t)=>e.keydownHandler(t.event)}"
        @mousedown="${(e,t)=>e.mousedownHandler(t.event)}"
    >
        <slot
            ${(0,s.slotted)({filter:dl.slottedOptionFilter,flatten:true,property:"slottedOptions"})}
        ></slot>
    </template>
`;class cl extends Fe{constructor(){super(...arguments);this.optionElements=[]}menuElementsChanged(){this.updateOptions()}headerElementsChanged(){this.updateOptions()}footerElementsChanged(){this.updateOptions()}updateOptions(){this.optionElements.splice(0,this.optionElements.length);this.addSlottedListItems(this.headerElements);this.addSlottedListItems(this.menuElements);this.addSlottedListItems(this.footerElements);this.$emit("optionsupdated",{bubbles:false})}addSlottedListItems(e){if(e===undefined){return}e.forEach((e=>{if(e.nodeType===1&&e.getAttribute("role")==="listitem"){e.id=e.id||nr("option-");this.optionElements.push(e)}}))}}f([s.observable],cl.prototype,"menuElements",void 0);f([s.observable],cl.prototype,"headerElements",void 0);f([s.observable],cl.prototype,"footerElements",void 0);f([s.observable],cl.prototype,"suggestionsAvailableText",void 0);const ul=s.html`
    <template>
        ${e=>e.value}
    </template>
`;class pl extends Fe{contentsTemplateChanged(){if(this.$fastController.isConnected){this.updateView()}}connectedCallback(){super.connectedCallback();this.updateView()}disconnectedCallback(){super.disconnectedCallback();this.disconnectView()}handleClick(e){if(e.defaultPrevented){return false}this.handleInvoked();return false}handleInvoked(){this.$emit("pickeroptioninvoked")}updateView(){var e,t;this.disconnectView();this.customView=(t=(e=this.contentsTemplate)===null||e===void 0?void 0:e.render(this,this))!==null&&t!==void 0?t:ul.render(this,this)}disconnectView(){var e;(e=this.customView)===null||e===void 0?void 0:e.dispose();this.customView=undefined}}f([(0,s.attr)({attribute:"value"})],pl.prototype,"value",void 0);f([s.observable],pl.prototype,"contentsTemplate",void 0);class fl extends Fe{}const ml=s.html`
    <template>
        ${e=>e.value}
    </template>
`;class vl extends Fe{contentsTemplateChanged(){if(this.$fastController.isConnected){this.updateView()}}connectedCallback(){super.connectedCallback();this.updateView()}disconnectedCallback(){this.disconnectView();super.disconnectedCallback()}handleKeyDown(e){if(e.defaultPrevented){return false}if(e.key===oi){this.handleInvoke();return false}return true}handleClick(e){if(!e.defaultPrevented){this.handleInvoke()}return false}handleInvoke(){this.$emit("pickeriteminvoked")}updateView(){var e,t;this.disconnectView();this.customView=(t=(e=this.contentsTemplate)===null||e===void 0?void 0:e.render(this,this))!==null&&t!==void 0?t:ml.render(this,this)}disconnectView(){var e;(e=this.customView)===null||e===void 0?void 0:e.dispose();this.customView=undefined}}f([(0,s.attr)({attribute:"value"})],vl.prototype,"value",void 0);f([s.observable],vl.prototype,"contentsTemplate",void 0);function bl(e){const t=e.tagFor(vl);return s.html`
    <${t}
        value="${e=>e}"
        :contentsTemplate="${(e,t)=>t.parent.listItemContentsTemplate}"
    >
    </${t}>
    `}function gl(e){const t=e.tagFor(pl);return s.html`
    <${t}
        value="${e=>e}"
        :contentsTemplate="${(e,t)=>t.parent.menuOptionContentsTemplate}"
    >
    </${t}>
    `}const yl=(e,t)=>{const i=e.tagFor(ro);const n=e.tagFor(cl);const o=e.tagFor(fl);const r=e.tagFor(fl);const a=bl(e);const l=gl(e);return s.html`
        <template
            :selectedListTag="${()=>o}"
            :menuTag="${()=>n}"
            :defaultListItemTemplate="${a}"
            :defaultMenuOptionTemplate="${l}"
            @focusin="${(e,t)=>e.handleFocusIn(t.event)}"
            @focusout="${(e,t)=>e.handleFocusOut(t.event)}"
            @keydown="${(e,t)=>e.handleKeyDown(t.event)}"
            @pickeriteminvoked="${(e,t)=>e.handleItemInvoke(t.event)}"
            @pickeroptioninvoked="${(e,t)=>e.handleOptionInvoke(t.event)}"
        >
            <slot name="list-region"></slot>

            ${(0,s.when)((e=>e.flyoutOpen),s.html`
                <${i}
                    class="region"
                    part="region"
                    auto-update-mode="${e=>e.menuConfig.autoUpdateMode}"
                    fixed-placement="${e=>e.menuConfig.fixedPlacement}"
                    vertical-positioning-mode="${e=>e.menuConfig.verticalPositioningMode}"
                    vertical-default-position="${e=>e.menuConfig.verticalDefaultPosition}"
                    vertical-scaling="${e=>e.menuConfig.verticalScaling}"
                    vertical-inset="${e=>e.menuConfig.verticalInset}"
                    vertical-viewport-lock="${e=>e.menuConfig.verticalViewportLock}"
                    horizontal-positioning-mode="${e=>e.menuConfig.horizontalPositioningMode}"
                    horizontal-default-position="${e=>e.menuConfig.horizontalDefaultPosition}"
                    horizontal-scaling="${e=>e.menuConfig.horizontalScaling}"
                    horizontal-inset="${e=>e.menuConfig.horizontalInset}"
                    horizontal-viewport-lock="${e=>e.menuConfig.horizontalViewportLock}"
                    @loaded="${(e,t)=>e.handleRegionLoaded(t.event)}"
                    ${(0,s.ref)("region")}
                >
                    ${(0,s.when)((e=>!e.showNoOptions&&!e.showLoading),s.html`
                            <slot name="menu-region"></slot>
                        `)}
                    ${(0,s.when)((e=>e.showNoOptions&&!e.showLoading),s.html`
                            <div class="no-options-display" part="no-options-display">
                                <slot name="no-options-region">
                                    ${e=>e.noSuggestionsText}
                                </slot>
                            </div>
                        `)}
                    ${(0,s.when)((e=>e.showLoading),s.html`
                            <div class="loading-display" part="loading-display">
                                <slot name="loading-region">
                                    <${r}
                                        part="loading-progress"
                                        class="loading-progress
                                        slot="loading-region"
                                    ></${r}>
                                        ${e=>e.loadingText}
                                </slot>
                            </div>
                        `)}
                </${i}>
            `)}
        </template>
    `};class Cl extends Fe{}class xl extends(To(Cl)){constructor(){super(...arguments);this.proxy=document.createElement("input")}}const wl=s.html`
    <input
        slot="input-region"
        role="combobox"
        type="text"
        autocapitalize="off"
        autocomplete="off"
        haspopup="list"
        aria-label="${e=>e.label}"
        aria-labelledby="${e=>e.labelledBy}"
        placeholder="${e=>e.placeholder}"
        ${(0,s.ref)("inputElement")}
    ></input>
`;class $l extends xl{constructor(){super(...arguments);this.selection="";this.filterSelected=true;this.filterQuery=true;this.noSuggestionsText="No suggestions available";this.suggestionsAvailableText="Suggestions available";this.loadingText="Loading suggestions";this.menuPlacement="bottom-fill";this.showLoading=false;this.optionsList=[];this.filteredOptionsList=[];this.flyoutOpen=false;this.menuFocusIndex=-1;this.showNoOptions=false;this.selectedItems=[];this.inputElementView=null;this.handleTextInput=e=>{this.query=this.inputElement.value};this.handleInputClick=e=>{e.preventDefault();this.toggleFlyout(true)};this.setRegionProps=()=>{if(!this.flyoutOpen){return}if(this.region===null||this.region===undefined){s.DOM.queueUpdate(this.setRegionProps);return}this.region.anchorElement=this.inputElement};this.configLookup={top:lo,bottom:ho,tallest:co,"top-fill":uo,"bottom-fill":po,"tallest-fill":fo}}selectionChanged(){if(this.$fastController.isConnected){this.handleSelectionChange();if(this.proxy instanceof HTMLInputElement){this.proxy.value=this.selection;this.validate()}}}optionsChanged(){this.optionsList=this.options.split(",").map((e=>e.trim())).filter((e=>e!==""))}menuPlacementChanged(){if(this.$fastController.isConnected){this.updateMenuConfig()}}showLoadingChanged(){if(this.$fastController.isConnected){s.DOM.queueUpdate((()=>{this.setFocusedOption(0)}))}}listItemTemplateChanged(){this.updateListItemTemplate()}defaultListItemTemplateChanged(){this.updateListItemTemplate()}menuOptionTemplateChanged(){this.updateOptionTemplate()}defaultMenuOptionTemplateChanged(){this.updateOptionTemplate()}optionsListChanged(){this.updateFilteredOptions()}queryChanged(){if(this.$fastController.isConnected){if(this.inputElement.value!==this.query){this.inputElement.value=this.query}this.updateFilteredOptions();this.$emit("querychange",{bubbles:false})}}filteredOptionsListChanged(){if(this.$fastController.isConnected){this.showNoOptions=this.filteredOptionsList.length===0&&this.menuElement.querySelectorAll('[role="listitem"]').length===0;this.setFocusedOption(this.showNoOptions?-1:0)}}flyoutOpenChanged(){if(this.flyoutOpen){s.DOM.queueUpdate(this.setRegionProps);this.$emit("menuopening",{bubbles:false})}else{this.$emit("menuclosing",{bubbles:false})}}showNoOptionsChanged(){if(this.$fastController.isConnected){s.DOM.queueUpdate((()=>{this.setFocusedOption(0)}))}}connectedCallback(){super.connectedCallback();this.listElement=document.createElement(this.selectedListTag);this.appendChild(this.listElement);this.itemsPlaceholderElement=document.createComment("");this.listElement.append(this.itemsPlaceholderElement);this.inputElementView=wl.render(this,this.listElement);const e=this.menuTag.toUpperCase();this.menuElement=Array.from(this.children).find((t=>t.tagName===e));if(this.menuElement===undefined){this.menuElement=document.createElement(this.menuTag);this.appendChild(this.menuElement)}if(this.menuElement.id===""){this.menuElement.id=nr("listbox-")}this.menuId=this.menuElement.id;this.optionsPlaceholder=document.createComment("");this.menuElement.append(this.optionsPlaceholder);this.updateMenuConfig();s.DOM.queueUpdate((()=>this.initialize()))}disconnectedCallback(){super.disconnectedCallback();this.toggleFlyout(false);this.inputElement.removeEventListener("input",this.handleTextInput);this.inputElement.removeEventListener("click",this.handleInputClick);if(this.inputElementView!==null){this.inputElementView.dispose();this.inputElementView=null}}focus(){this.inputElement.focus()}initialize(){this.updateListItemTemplate();this.updateOptionTemplate();this.itemsRepeatBehavior=new s.RepeatDirective((e=>e.selectedItems),(e=>e.activeListItemTemplate),{positioning:true}).createBehavior(this.itemsPlaceholderElement);this.inputElement.addEventListener("input",this.handleTextInput);this.inputElement.addEventListener("click",this.handleInputClick);this.$fastController.addBehaviors([this.itemsRepeatBehavior]);this.menuElement.suggestionsAvailableText=this.suggestionsAvailableText;this.menuElement.addEventListener("optionsupdated",this.handleMenuOptionsUpdated);this.optionsRepeatBehavior=new s.RepeatDirective((e=>e.filteredOptionsList),(e=>e.activeMenuOptionTemplate),{positioning:true}).createBehavior(this.optionsPlaceholder);this.$fastController.addBehaviors([this.optionsRepeatBehavior]);this.handleSelectionChange()}toggleFlyout(e){if(this.flyoutOpen===e){return}if(e&&document.activeElement===this.inputElement){this.flyoutOpen=e;s.DOM.queueUpdate((()=>{if(this.menuElement!==undefined){this.setFocusedOption(0)}else{this.disableMenu()}}));return}this.flyoutOpen=false;this.disableMenu();return}handleMenuOptionsUpdated(e){e.preventDefault();if(this.flyoutOpen){this.setFocusedOption(0)}}handleKeyDown(e){if(e.defaultPrevented){return false}switch(e.key){case ti:{if(!this.flyoutOpen){this.toggleFlyout(true)}else{const e=this.flyoutOpen?Math.min(this.menuFocusIndex+1,this.menuElement.optionElements.length-1):0;this.setFocusedOption(e)}return false}case ni:{if(!this.flyoutOpen){this.toggleFlyout(true)}else{const e=this.flyoutOpen?Math.max(this.menuFocusIndex-1,0):0;this.setFocusedOption(e)}return false}case ri:{this.toggleFlyout(false);return false}case oi:{if(this.menuFocusIndex!==-1&&this.menuElement.optionElements.length>this.menuFocusIndex){this.menuElement.optionElements[this.menuFocusIndex].click()}return false}case si:{if(document.activeElement!==this.inputElement){this.incrementFocusedItem(1);return false}return true}case ii:{if(this.inputElement.selectionStart===0){this.incrementFocusedItem(-1);return false}return true}case mi:case fi:{if(document.activeElement===null){return true}if(document.activeElement===this.inputElement){if(this.inputElement.selectionStart===0){this.selection=this.selectedItems.slice(0,this.selectedItems.length-1).toString();this.toggleFlyout(false);return false}return true}const e=Array.from(this.listElement.children);const t=e.indexOf(document.activeElement);if(t>-1){this.selection=this.selectedItems.splice(t,1).toString();s.DOM.queueUpdate((()=>{e[Math.min(e.length,t)].focus()}));return false}return true}}this.toggleFlyout(true);return true}handleFocusIn(e){return false}handleFocusOut(e){if(this.menuElement===undefined||!this.menuElement.contains(e.relatedTarget)){this.toggleFlyout(false)}return false}handleSelectionChange(){if(this.selectedItems.toString()===this.selection){return}this.selectedItems=this.selection===""?[]:this.selection.split(",");this.updateFilteredOptions();s.DOM.queueUpdate((()=>{this.checkMaxItems()}));this.$emit("selectionchange",{bubbles:false})}handleRegionLoaded(e){s.DOM.queueUpdate((()=>{this.setFocusedOption(0);this.$emit("menuloaded",{bubbles:false})}))}checkMaxItems(){if(this.inputElement===undefined){return}if(this.maxSelected!==undefined&&this.selectedItems.length>=this.maxSelected){if(document.activeElement===this.inputElement){const e=Array.from(this.listElement.querySelectorAll("[role='listitem']"));e[e.length-1].focus()}this.inputElement.hidden=true}else{this.inputElement.hidden=false}}handleItemInvoke(e){if(e.defaultPrevented){return false}if(e.target instanceof vl){const t=Array.from(this.listElement.querySelectorAll("[role='listitem']"));const i=t.indexOf(e.target);if(i!==-1){const e=this.selectedItems.slice();e.splice(i,1);this.selection=e.toString();s.DOM.queueUpdate((()=>this.incrementFocusedItem(0)))}return false}return true}handleOptionInvoke(e){if(e.defaultPrevented){return false}if(e.target instanceof pl){if(e.target.value!==undefined){this.selection=`${this.selection}${this.selection===""?"":","}${e.target.value}`}this.inputElement.value="";this.query="";this.inputElement.focus();this.toggleFlyout(false);return false}return true}incrementFocusedItem(e){if(this.selectedItems.length===0){this.inputElement.focus();return}const t=Array.from(this.listElement.querySelectorAll("[role='listitem']"));if(document.activeElement!==null){let i=t.indexOf(document.activeElement);if(i===-1){i=t.length}const s=Math.min(t.length,Math.max(0,i+e));if(s===t.length){if(this.maxSelected!==undefined&&this.selectedItems.length>=this.maxSelected){t[s-1].focus()}else{this.inputElement.focus()}}else{t[s].focus()}}}disableMenu(){var e,t,i;this.menuFocusIndex=-1;this.menuFocusOptionId=undefined;(e=this.inputElement)===null||e===void 0?void 0:e.removeAttribute("aria-activedescendant");(t=this.inputElement)===null||t===void 0?void 0:t.removeAttribute("aria-owns");(i=this.inputElement)===null||i===void 0?void 0:i.removeAttribute("aria-expanded")}setFocusedOption(e){if(!this.flyoutOpen||e===-1||this.showNoOptions||this.showLoading){this.disableMenu();return}if(this.menuElement.optionElements.length===0){return}this.menuElement.optionElements.forEach((e=>{e.setAttribute("aria-selected","false")}));this.menuFocusIndex=e;if(this.menuFocusIndex>this.menuElement.optionElements.length-1){this.menuFocusIndex=this.menuElement.optionElements.length-1}this.menuFocusOptionId=this.menuElement.optionElements[this.menuFocusIndex].id;this.inputElement.setAttribute("aria-owns",this.menuId);this.inputElement.setAttribute("aria-expanded","true");this.inputElement.setAttribute("aria-activedescendant",this.menuFocusOptionId);const t=this.menuElement.optionElements[this.menuFocusIndex];t.setAttribute("aria-selected","true");this.menuElement.scrollTo(0,t.offsetTop)}updateListItemTemplate(){var e;this.activeListItemTemplate=(e=this.listItemTemplate)!==null&&e!==void 0?e:this.defaultListItemTemplate}updateOptionTemplate(){var e;this.activeMenuOptionTemplate=(e=this.menuOptionTemplate)!==null&&e!==void 0?e:this.defaultMenuOptionTemplate}updateFilteredOptions(){this.filteredOptionsList=this.optionsList.slice(0);if(this.filterSelected){this.filteredOptionsList=this.filteredOptionsList.filter((e=>this.selectedItems.indexOf(e)===-1))}if(this.filterQuery&&this.query!==""&&this.query!==undefined){this.filteredOptionsList=this.filteredOptionsList.filter((e=>e.indexOf(this.query)!==-1))}}updateMenuConfig(){let e=this.configLookup[this.menuPlacement];if(e===null){e=po}this.menuConfig=Object.assign(Object.assign({},e),{autoUpdateMode:"auto",fixedPlacement:true,horizontalViewportLock:false,verticalViewportLock:false})}}f([(0,s.attr)({attribute:"selection"})],$l.prototype,"selection",void 0);f([(0,s.attr)({attribute:"options"})],$l.prototype,"options",void 0);f([(0,s.attr)({attribute:"filter-selected",mode:"boolean"})],$l.prototype,"filterSelected",void 0);f([(0,s.attr)({attribute:"filter-query",mode:"boolean"})],$l.prototype,"filterQuery",void 0);f([(0,s.attr)({attribute:"max-selected"})],$l.prototype,"maxSelected",void 0);f([(0,s.attr)({attribute:"no-suggestions-text"})],$l.prototype,"noSuggestionsText",void 0);f([(0,s.attr)({attribute:"suggestions-available-text"})],$l.prototype,"suggestionsAvailableText",void 0);f([(0,s.attr)({attribute:"loading-text"})],$l.prototype,"loadingText",void 0);f([(0,s.attr)({attribute:"label"})],$l.prototype,"label",void 0);f([(0,s.attr)({attribute:"labelledby"})],$l.prototype,"labelledBy",void 0);f([(0,s.attr)({attribute:"placeholder"})],$l.prototype,"placeholder",void 0);f([(0,s.attr)({attribute:"menu-placement"})],$l.prototype,"menuPlacement",void 0);f([s.observable],$l.prototype,"showLoading",void 0);f([s.observable],$l.prototype,"listItemTemplate",void 0);f([s.observable],$l.prototype,"defaultListItemTemplate",void 0);f([s.observable],$l.prototype,"activeListItemTemplate",void 0);f([s.observable],$l.prototype,"menuOptionTemplate",void 0);f([s.observable],$l.prototype,"defaultMenuOptionTemplate",void 0);f([s.observable],$l.prototype,"activeMenuOptionTemplate",void 0);f([s.observable],$l.prototype,"listItemContentsTemplate",void 0);f([s.observable],$l.prototype,"menuOptionContentsTemplate",void 0);f([s.observable],$l.prototype,"optionsList",void 0);f([s.observable],$l.prototype,"query",void 0);f([s.observable],$l.prototype,"filteredOptionsList",void 0);f([s.observable],$l.prototype,"flyoutOpen",void 0);f([s.observable],$l.prototype,"menuId",void 0);f([s.observable],$l.prototype,"selectedListTag",void 0);f([s.observable],$l.prototype,"menuTag",void 0);f([s.observable],$l.prototype,"menuFocusIndex",void 0);f([s.observable],$l.prototype,"menuFocusOptionId",void 0);f([s.observable],$l.prototype,"showNoOptions",void 0);f([s.observable],$l.prototype,"menuConfig",void 0);f([s.observable],$l.prototype,"selectedItems",void 0);const kl=(e,t)=>s.html`
        <template role="list" slot="menu-region">
            <div class="options-display" part="options-display">
                <div class="header-region" part="header-region">
                    <slot name="header-region" ${(0,s.slotted)("headerElements")}></slot>
                </div>

                <slot ${(0,s.slotted)("menuElements")}></slot>
                <div class="footer-region" part="footer-region">
                    <slot name="footer-region" ${(0,s.slotted)("footerElements")}></slot>
                </div>
                <div
                    role="alert"
                    aria-live="polite"
                    part="suggestions-available-alert"
                    class="suggestions-available-alert"
                >
                    ${e=>e.suggestionsAvailableText}
                </div>
            </div>
        </template>
    `;const Il=(e,t)=>s.html`
        <template
            role="listitem"
            tabindex="-1"
            @click="${(e,t)=>e.handleClick(t.event)}"
        >
            <slot></slot>
        </template>
    `;const El=(e,t)=>s.html`
        <template slot="list-region" role="list" class="picker-list">
            <slot></slot>
            <slot name="input-region"></slot>
        </template>
    `;const Ol=(e,t)=>s.html`
        <template
            role="listitem"
            tabindex="0"
            @click="${(e,t)=>e.handleClick(t.event)}"
            @keydown="${(e,t)=>e.handleKeyDown(t.event)}"
        >
            <slot></slot>
        </template>
    `;const Tl={menuitem:"menuitem",menuitemcheckbox:"menuitemcheckbox",menuitemradio:"menuitemradio"};const Rl={[Tl.menuitem]:"menuitem",[Tl.menuitemcheckbox]:"menuitemcheckbox",[Tl.menuitemradio]:"menuitemradio"};const Sl=(e,t)=>s.html`
    <template
        role="${e=>e.role}"
        aria-haspopup="${e=>e.hasSubmenu?"menu":void 0}"
        aria-checked="${e=>e.role!==Tl.menuitem?e.checked:void 0}"
        aria-disabled="${e=>e.disabled}"
        aria-expanded="${e=>e.expanded}"
        @keydown="${(e,t)=>e.handleMenuItemKeyDown(t.event)}"
        @click="${(e,t)=>e.handleMenuItemClick(t.event)}"
        @mouseover="${(e,t)=>e.handleMouseOver(t.event)}"
        @mouseout="${(e,t)=>e.handleMouseOut(t.event)}"
        class="${e=>e.disabled?"disabled":""} ${e=>e.expanded?"expanded":""} ${e=>`indent-${e.startColumnCount}`}"
    >
            ${(0,s.when)((e=>e.role===Tl.menuitemcheckbox),s.html`
                    <div part="input-container" class="input-container">
                        <span part="checkbox" class="checkbox">
                            <slot name="checkbox-indicator">
                                ${t.checkboxIndicator||""}
                            </slot>
                        </span>
                    </div>
                `)}
            ${(0,s.when)((e=>e.role===Tl.menuitemradio),s.html`
                    <div part="input-container" class="input-container">
                        <span part="radio" class="radio">
                            <slot name="radio-indicator">
                                ${t.radioIndicator||""}
                            </slot>
                        </span>
                    </div>
                `)}
        </div>
        ${r(e,t)}
        <span class="content" part="content">
            <slot></slot>
        </span>
        ${o(e,t)}
        ${(0,s.when)((e=>e.hasSubmenu),s.html`
                <div
                    part="expand-collapse-glyph-container"
                    class="expand-collapse-glyph-container"
                >
                    <span part="expand-collapse" class="expand-collapse">
                        <slot name="expand-collapse-indicator">
                            ${t.expandCollapseGlyph||""}
                        </slot>
                    </span>
                </div>
            `)}
        ${(0,s.when)((e=>e.expanded),s.html`
                <${e.tagFor(ro)}
                    :anchorElement="${e=>e}"
                    vertical-positioning-mode="dynamic"
                    vertical-default-position="bottom"
                    vertical-inset="true"
                    horizontal-positioning-mode="dynamic"
                    horizontal-default-position="end"
                    class="submenu-region"
                    dir="${e=>e.currentDirection}"
                    @loaded="${e=>e.submenuLoaded()}"
                    ${(0,s.ref)("submenuRegion")}
                    part="submenu-region"
                >
                    <slot name="submenu"></slot>
                </${e.tagFor(ro)}>
            `)}
    </template>
`;class Dl extends Fe{constructor(){super(...arguments);this.role=Tl.menuitem;this.hasSubmenu=false;this.currentDirection=Oi.N.ltr;this.focusSubmenuOnLoad=false;this.handleMenuItemKeyDown=e=>{if(e.defaultPrevented){return false}switch(e.key){case oi:case ui:this.invoke();return false;case si:this.expandAndFocus();return false;case ii:if(this.expanded){this.expanded=false;this.focus();return false}}return true};this.handleMenuItemClick=e=>{if(e.defaultPrevented||this.disabled){return false}this.invoke();return false};this.submenuLoaded=()=>{if(!this.focusSubmenuOnLoad){return}this.focusSubmenuOnLoad=false;if(this.hasSubmenu){this.submenu.focus();this.setAttribute("tabindex","-1")}};this.handleMouseOver=e=>{if(this.disabled||!this.hasSubmenu||this.expanded){return false}this.expanded=true;return false};this.handleMouseOut=e=>{if(!this.expanded||this.contains(document.activeElement)){return false}this.expanded=false;return false};this.expandAndFocus=()=>{if(!this.hasSubmenu){return}this.focusSubmenuOnLoad=true;this.expanded=true};this.invoke=()=>{if(this.disabled){return}switch(this.role){case Tl.menuitemcheckbox:this.checked=!this.checked;break;case Tl.menuitem:this.updateSubmenu();if(this.hasSubmenu){this.expandAndFocus()}else{this.$emit("change")}break;case Tl.menuitemradio:if(!this.checked){this.checked=true}break}};this.updateSubmenu=()=>{this.submenu=this.domChildren().find((e=>e.getAttribute("role")==="menu"));this.hasSubmenu=this.submenu===undefined?false:true}}expandedChanged(e){if(this.$fastController.isConnected){if(this.submenu===undefined){return}if(this.expanded===false){this.submenu.collapseExpandedItem()}else{this.currentDirection=no(this)}this.$emit("expanded-change",this,{bubbles:false})}}checkedChanged(e,t){if(this.$fastController.isConnected){this.$emit("change")}}connectedCallback(){super.connectedCallback();s.DOM.queueUpdate((()=>{this.updateSubmenu()}));if(!this.startColumnCount){this.startColumnCount=1}this.observer=new MutationObserver(this.updateSubmenu)}disconnectedCallback(){super.disconnectedCallback();this.submenu=undefined;if(this.observer!==undefined){this.observer.disconnect();this.observer=undefined}}domChildren(){return Array.from(this.children).filter((e=>!e.hasAttribute("hidden")))}}f([(0,s.attr)({mode:"boolean"})],Dl.prototype,"disabled",void 0);f([(0,s.attr)({mode:"boolean"})],Dl.prototype,"expanded",void 0);f([s.observable],Dl.prototype,"startColumnCount",void 0);f([s.attr],Dl.prototype,"role",void 0);f([(0,s.attr)({mode:"boolean"})],Dl.prototype,"checked",void 0);f([s.observable],Dl.prototype,"submenuRegion",void 0);f([s.observable],Dl.prototype,"hasSubmenu",void 0);f([s.observable],Dl.prototype,"currentDirection",void 0);f([s.observable],Dl.prototype,"submenu",void 0);Me(Dl,n);const Al=(e,t)=>s.html`
    <template
        slot="${e=>e.slot?e.slot:e.isNestedMenu()?"submenu":void 0}"
        role="menu"
        @keydown="${(e,t)=>e.handleMenuKeyDown(t.event)}"
        @focusout="${(e,t)=>e.handleFocusOut(t.event)}"
    >
        <slot ${(0,s.slotted)("items")}></slot>
    </template>
`;class Fl extends Fe{constructor(){super(...arguments);this.expandedItem=null;this.focusIndex=-1;this.isNestedMenu=()=>this.parentElement!==null&&ur(this.parentElement)&&this.parentElement.getAttribute("role")==="menuitem";this.handleFocusOut=e=>{if(!this.contains(e.relatedTarget)&&this.menuItems!==undefined){this.collapseExpandedItem();const e=this.menuItems.findIndex(this.isFocusableElement);this.menuItems[this.focusIndex].setAttribute("tabindex","-1");this.menuItems[e].setAttribute("tabindex","0");this.focusIndex=e}};this.handleItemFocus=e=>{const t=e.target;if(this.menuItems!==undefined&&t!==this.menuItems[this.focusIndex]){this.menuItems[this.focusIndex].setAttribute("tabindex","-1");this.focusIndex=this.menuItems.indexOf(t);t.setAttribute("tabindex","0")}};this.handleExpandedChanged=e=>{if(e.defaultPrevented||e.target===null||this.menuItems===undefined||this.menuItems.indexOf(e.target)<0){return}e.preventDefault();const t=e.target;if(this.expandedItem!==null&&t===this.expandedItem&&t.expanded===false){this.expandedItem=null;return}if(t.expanded){if(this.expandedItem!==null&&this.expandedItem!==t){this.expandedItem.expanded=false}this.menuItems[this.focusIndex].setAttribute("tabindex","-1");this.expandedItem=t;this.focusIndex=this.menuItems.indexOf(t);t.setAttribute("tabindex","0")}};this.removeItemListeners=()=>{if(this.menuItems!==undefined){this.menuItems.forEach((e=>{e.removeEventListener("expanded-change",this.handleExpandedChanged);e.removeEventListener("focus",this.handleItemFocus)}))}};this.setItems=()=>{const e=this.domChildren();this.removeItemListeners();this.menuItems=e;const t=this.menuItems.filter(this.isMenuItemElement);if(t.length){this.focusIndex=0}function i(e){const t=e.getAttribute("role");const i=e.querySelector("[slot=start]");if(t!==Tl.menuitem&&i===null){return 1}else if(t===Tl.menuitem&&i!==null){return 1}else if(t!==Tl.menuitem&&i!==null){return 2}else{return 0}}const s=t.reduce(((e,t)=>{const s=i(t);return e>s?e:s}),0);t.forEach(((e,t)=>{e.setAttribute("tabindex",t===0?"0":"-1");e.addEventListener("expanded-change",this.handleExpandedChanged);e.addEventListener("focus",this.handleItemFocus);if(e instanceof Dl){e.startColumnCount=s}}))};this.changeHandler=e=>{if(this.menuItems===undefined){return}const t=e.target;const i=this.menuItems.indexOf(t);if(i===-1){return}if(t.role==="menuitemradio"&&t.checked===true){for(let t=i-1;t>=0;--t){const e=this.menuItems[t];const i=e.getAttribute("role");if(i===Tl.menuitemradio){e.checked=false}if(i==="separator"){break}}const e=this.menuItems.length-1;for(let t=i+1;t<=e;++t){const e=this.menuItems[t];const i=e.getAttribute("role");if(i===Tl.menuitemradio){e.checked=false}if(i==="separator"){break}}}};this.isMenuItemElement=e=>ur(e)&&Fl.focusableElementRoles.hasOwnProperty(e.getAttribute("role"));this.isFocusableElement=e=>this.isMenuItemElement(e)}itemsChanged(e,t){if(this.$fastController.isConnected&&this.menuItems!==undefined){this.setItems()}}connectedCallback(){super.connectedCallback();s.DOM.queueUpdate((()=>{this.setItems()}));this.addEventListener("change",this.changeHandler)}disconnectedCallback(){super.disconnectedCallback();this.removeItemListeners();this.menuItems=undefined;this.removeEventListener("change",this.changeHandler)}focus(){this.setFocus(0,1)}collapseExpandedItem(){if(this.expandedItem!==null){this.expandedItem.expanded=false;this.expandedItem=null}}handleMenuKeyDown(e){if(e.defaultPrevented||this.menuItems===undefined){return}switch(e.key){case ti:this.setFocus(this.focusIndex+1,1);return;case ni:this.setFocus(this.focusIndex-1,-1);return;case li:this.setFocus(this.menuItems.length-1,-1);return;case ai:this.setFocus(0,1);return;default:return true}}domChildren(){return Array.from(this.children).filter((e=>!e.hasAttribute("hidden")))}setFocus(e,t){if(this.menuItems===undefined){return}while(e>=0&&e<this.menuItems.length){const i=this.menuItems[e];if(this.isFocusableElement(i)){if(this.focusIndex>-1&&this.menuItems.length>=this.focusIndex-1){this.menuItems[this.focusIndex].setAttribute("tabindex","-1")}this.focusIndex=e;i.setAttribute("tabindex","0");i.focus();break}e+=t}}}Fl.focusableElementRoles=Rl;f([s.observable],Fl.prototype,"items",void 0);const Ll=(e,t)=>s.html`
    <template class="${e=>e.readOnly?"readonly":""}">
        <label
            part="label"
            for="control"
            class="${e=>e.defaultSlottedNodes&&e.defaultSlottedNodes.length?"label":"label label__hidden"}"
        >
            <slot ${(0,s.slotted)("defaultSlottedNodes")}></slot>
        </label>
        <div class="root" part="root">
            ${r(e,t)}
            <input
                class="control"
                part="control"
                id="control"
                @input="${e=>e.handleTextInput()}"
                @change="${e=>e.handleChange()}"
                @keydown="${(e,t)=>e.handleKeyDown(t.event)}"
                @blur="${(e,t)=>e.handleBlur()}"
                ?autofocus="${e=>e.autofocus}"
                ?disabled="${e=>e.disabled}"
                list="${e=>e.list}"
                maxlength="${e=>e.maxlength}"
                minlength="${e=>e.minlength}"
                placeholder="${e=>e.placeholder}"
                ?readonly="${e=>e.readOnly}"
                ?required="${e=>e.required}"
                size="${e=>e.size}"
                type="text"
                inputmode="numeric"
                min="${e=>e.min}"
                max="${e=>e.max}"
                step="${e=>e.step}"
                aria-atomic="${e=>e.ariaAtomic}"
                aria-busy="${e=>e.ariaBusy}"
                aria-controls="${e=>e.ariaControls}"
                aria-current="${e=>e.ariaCurrent}"
                aria-describedby="${e=>e.ariaDescribedby}"
                aria-details="${e=>e.ariaDetails}"
                aria-disabled="${e=>e.ariaDisabled}"
                aria-errormessage="${e=>e.ariaErrormessage}"
                aria-flowto="${e=>e.ariaFlowto}"
                aria-haspopup="${e=>e.ariaHaspopup}"
                aria-hidden="${e=>e.ariaHidden}"
                aria-invalid="${e=>e.ariaInvalid}"
                aria-keyshortcuts="${e=>e.ariaKeyshortcuts}"
                aria-label="${e=>e.ariaLabel}"
                aria-labelledby="${e=>e.ariaLabelledby}"
                aria-live="${e=>e.ariaLive}"
                aria-owns="${e=>e.ariaOwns}"
                aria-relevant="${e=>e.ariaRelevant}"
                aria-roledescription="${e=>e.ariaRoledescription}"
                ${(0,s.ref)("control")}
            />
            ${(0,s.when)((e=>!e.hideStep&&!e.readOnly&&!e.disabled),s.html`
                    <div class="controls" part="controls">
                        <div class="step-up" part="step-up" @click="${e=>e.stepUp()}">
                            <slot name="step-up-glyph">
                                ${t.stepUpGlyph||""}
                            </slot>
                        </div>
                        <div
                            class="step-down"
                            part="step-down"
                            @click="${e=>e.stepDown()}"
                        >
                            <slot name="step-down-glyph">
                                ${t.stepDownGlyph||""}
                            </slot>
                        </div>
                    </div>
                `)}
            ${o(e,t)}
        </div>
    </template>
`;class Pl extends Fe{}class Ml extends(To(Pl)){constructor(){super(...arguments);this.proxy=document.createElement("input")}}const Hl={email:"email",password:"password",tel:"tel",text:"text",url:"url"};class zl extends Ml{constructor(){super(...arguments);this.type=Hl.text}readOnlyChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.readOnly=this.readOnly;this.validate()}}autofocusChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.autofocus=this.autofocus;this.validate()}}placeholderChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.placeholder=this.placeholder}}typeChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.type=this.type;this.validate()}}listChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.setAttribute("list",this.list);this.validate()}}maxlengthChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.maxLength=this.maxlength;this.validate()}}minlengthChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.minLength=this.minlength;this.validate()}}patternChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.pattern=this.pattern;this.validate()}}sizeChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.size=this.size}}spellcheckChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.spellcheck=this.spellcheck}}connectedCallback(){super.connectedCallback();this.proxy.setAttribute("type",this.type);this.validate();if(this.autofocus){s.DOM.queueUpdate((()=>{this.focus()}))}}select(){this.control.select();this.$emit("select")}handleTextInput(){this.value=this.control.value}handleChange(){this.$emit("change")}validate(){super.validate(this.control)}}f([(0,s.attr)({attribute:"readonly",mode:"boolean"})],zl.prototype,"readOnly",void 0);f([(0,s.attr)({mode:"boolean"})],zl.prototype,"autofocus",void 0);f([s.attr],zl.prototype,"placeholder",void 0);f([s.attr],zl.prototype,"type",void 0);f([s.attr],zl.prototype,"list",void 0);f([(0,s.attr)({converter:s.nullableNumberConverter})],zl.prototype,"maxlength",void 0);f([(0,s.attr)({converter:s.nullableNumberConverter})],zl.prototype,"minlength",void 0);f([s.attr],zl.prototype,"pattern",void 0);f([(0,s.attr)({converter:s.nullableNumberConverter})],zl.prototype,"size",void 0);f([(0,s.attr)({mode:"boolean"})],zl.prototype,"spellcheck",void 0);f([s.observable],zl.prototype,"defaultSlottedNodes",void 0);class Vl{}Me(Vl,$i);Me(zl,n,Vl);class Nl extends Fe{}class Bl extends(To(Nl)){constructor(){super(...arguments);this.proxy=document.createElement("input")}}class Ul extends Bl{constructor(){super(...arguments);this.hideStep=false;this.step=1;this.isUserInput=false}maxChanged(e,t){var i;this.max=Math.max(t,(i=this.min)!==null&&i!==void 0?i:t);const s=Math.min(this.min,this.max);if(this.min!==undefined&&this.min!==s){this.min=s}this.value=this.getValidValue(this.value)}minChanged(e,t){var i;this.min=Math.min(t,(i=this.max)!==null&&i!==void 0?i:t);const s=Math.max(this.min,this.max);if(this.max!==undefined&&this.max!==s){this.max=s}this.value=this.getValidValue(this.value)}get valueAsNumber(){return parseFloat(super.value)}set valueAsNumber(e){this.value=e.toString()}valueChanged(e,t){this.value=this.getValidValue(t);if(t!==this.value){return}if(this.control&&!this.isUserInput){this.control.value=this.value}super.valueChanged(e,this.value);if(e!==undefined&&!this.isUserInput){this.$emit("input");this.$emit("change")}this.isUserInput=false}validate(){super.validate(this.control)}getValidValue(e){var t,i;let s=parseFloat(parseFloat(e).toPrecision(12));if(isNaN(s)){s=""}else{s=Math.min(s,(t=this.max)!==null&&t!==void 0?t:s);s=Math.max(s,(i=this.min)!==null&&i!==void 0?i:s).toString()}return s}stepUp(){const e=parseFloat(this.value);const t=!isNaN(e)?e+this.step:this.min>0?this.min:this.max<0?this.max:!this.min?this.step:0;this.value=t.toString()}stepDown(){const e=parseFloat(this.value);const t=!isNaN(e)?e-this.step:this.min>0?this.min:this.max<0?this.max:!this.min?0-this.step:0;this.value=t.toString()}connectedCallback(){super.connectedCallback();this.proxy.setAttribute("type","number");this.validate();this.control.value=this.value;if(this.autofocus){s.DOM.queueUpdate((()=>{this.focus()}))}}select(){this.control.select();this.$emit("select")}handleTextInput(){this.control.value=this.control.value.replace(/[^0-9\-+e.]/g,"");this.isUserInput=true;this.value=this.control.value}handleChange(){this.$emit("change")}handleKeyDown(e){const t=e.key;switch(t){case ni:this.stepUp();return false;case ti:this.stepDown();return false}return true}handleBlur(){this.control.value=this.value}}f([(0,s.attr)({attribute:"readonly",mode:"boolean"})],Ul.prototype,"readOnly",void 0);f([(0,s.attr)({mode:"boolean"})],Ul.prototype,"autofocus",void 0);f([(0,s.attr)({attribute:"hide-step",mode:"boolean"})],Ul.prototype,"hideStep",void 0);f([s.attr],Ul.prototype,"placeholder",void 0);f([s.attr],Ul.prototype,"list",void 0);f([(0,s.attr)({converter:s.nullableNumberConverter})],Ul.prototype,"maxlength",void 0);f([(0,s.attr)({converter:s.nullableNumberConverter})],Ul.prototype,"minlength",void 0);f([(0,s.attr)({converter:s.nullableNumberConverter})],Ul.prototype,"size",void 0);f([(0,s.attr)({converter:s.nullableNumberConverter})],Ul.prototype,"step",void 0);f([(0,s.attr)({converter:s.nullableNumberConverter})],Ul.prototype,"max",void 0);f([(0,s.attr)({converter:s.nullableNumberConverter})],Ul.prototype,"min",void 0);f([s.observable],Ul.prototype,"defaultSlottedNodes",void 0);Me(Ul,n,Vl);const ql=44;const jl=(e,t)=>s.html`
    <template
        role="progressbar"
        aria-valuenow="${e=>e.value}"
        aria-valuemin="${e=>e.min}"
        aria-valuemax="${e=>e.max}"
        class="${e=>e.paused?"paused":""}"
    >
        ${(0,s.when)((e=>typeof e.value==="number"),s.html`
                <svg
                    class="progress"
                    part="progress"
                    viewBox="0 0 16 16"
                    slot="determinate"
                >
                    <circle
                        class="background"
                        part="background"
                        cx="8px"
                        cy="8px"
                        r="7px"
                    ></circle>
                    <circle
                        class="determinate"
                        part="determinate"
                        style="stroke-dasharray: ${e=>ql*e.percentComplete/100}px ${ql}px"
                        cx="8px"
                        cy="8px"
                        r="7px"
                    ></circle>
                </svg>
            `,s.html`
                <slot name="indeterminate" slot="indeterminate">
                    ${t.indeterminateIndicator||""}
                </slot>
            `)}
    </template>
`;class _l extends Fe{constructor(){super(...arguments);this.percentComplete=0}valueChanged(){if(this.$fastController.isConnected){this.updatePercentComplete()}}minChanged(){if(this.$fastController.isConnected){this.updatePercentComplete()}}maxChanged(){if(this.$fastController.isConnected){this.updatePercentComplete()}}connectedCallback(){super.connectedCallback();this.updatePercentComplete()}updatePercentComplete(){const e=typeof this.min==="number"?this.min:0;const t=typeof this.max==="number"?this.max:100;const i=typeof this.value==="number"?this.value:0;const s=t-e;this.percentComplete=s===0?0:Math.fround((i-e)/s*100)}}f([(0,s.attr)({converter:s.nullableNumberConverter})],_l.prototype,"value",void 0);f([(0,s.attr)({converter:s.nullableNumberConverter})],_l.prototype,"min",void 0);f([(0,s.attr)({converter:s.nullableNumberConverter})],_l.prototype,"max",void 0);f([(0,s.attr)({mode:"boolean"})],_l.prototype,"paused",void 0);f([s.observable],_l.prototype,"percentComplete",void 0);const Kl=(e,t)=>s.html`
    <template
        role="progressbar"
        aria-valuenow="${e=>e.value}"
        aria-valuemin="${e=>e.min}"
        aria-valuemax="${e=>e.max}"
        class="${e=>e.paused?"paused":""}"
    >
        ${(0,s.when)((e=>typeof e.value==="number"),s.html`
                <div class="progress" part="progress" slot="determinate">
                    <div
                        class="determinate"
                        part="determinate"
                        style="width: ${e=>e.percentComplete}%"
                    ></div>
                </div>
            `,s.html`
                <div class="progress" part="progress" slot="indeterminate">
                    <slot class="indeterminate" name="indeterminate">
                        ${t.indeterminateIndicator1||""}
                        ${t.indeterminateIndicator2||""}
                    </slot>
                </div>
            `)}
    </template>
`;const Wl=(e,t)=>s.html`
    <template
        role="radiogroup"
        aria-disabled="${e=>e.disabled}"
        aria-readonly="${e=>e.readOnly}"
        @click="${(e,t)=>e.clickHandler(t.event)}"
        @keydown="${(e,t)=>e.keydownHandler(t.event)}"
        @focusout="${(e,t)=>e.focusOutHandler(t.event)}"
    >
        <slot name="label"></slot>
        <div
            class="positioning-region ${e=>e.orientation===il.i.horizontal?"horizontal":"vertical"}"
            part="positioning-region"
        >
            <slot
                ${(0,s.slotted)({property:"slottedRadioButtons",filter:(0,s.elements)("[role=radio]")})}
            ></slot>
        </div>
    </template>
`;class Gl extends Fe{constructor(){super(...arguments);this.orientation=il.i.horizontal;this.radioChangeHandler=e=>{const t=e.target;if(t.checked){this.slottedRadioButtons.forEach((e=>{if(e!==t){e.checked=false;if(!this.isInsideFoundationToolbar){e.setAttribute("tabindex","-1")}}}));this.selectedRadio=t;this.value=t.value;t.setAttribute("tabindex","0");this.focusedRadio=t}e.stopPropagation()};this.moveToRadioByIndex=(e,t)=>{const i=e[t];if(!this.isInsideToolbar){i.setAttribute("tabindex","0");if(i.readOnly){this.slottedRadioButtons.forEach((e=>{if(e!==i){e.setAttribute("tabindex","-1")}}))}else{i.checked=true;this.selectedRadio=i}}this.focusedRadio=i;i.focus()};this.moveRightOffGroup=()=>{var e;(e=this.nextElementSibling)===null||e===void 0?void 0:e.focus()};this.moveLeftOffGroup=()=>{var e;(e=this.previousElementSibling)===null||e===void 0?void 0:e.focus()};this.focusOutHandler=e=>{const t=this.slottedRadioButtons;const i=e.target;const s=i!==null?t.indexOf(i):0;const n=this.focusedRadio?t.indexOf(this.focusedRadio):-1;if(n===0&&s===n||n===t.length-1&&n===s){if(!this.selectedRadio){this.focusedRadio=t[0];this.focusedRadio.setAttribute("tabindex","0");t.forEach((e=>{if(e!==this.focusedRadio){e.setAttribute("tabindex","-1")}}))}else{this.focusedRadio=this.selectedRadio;if(!this.isInsideFoundationToolbar){this.selectedRadio.setAttribute("tabindex","0");t.forEach((e=>{if(e!==this.selectedRadio){e.setAttribute("tabindex","-1")}}))}}}return true};this.clickHandler=e=>{const t=e.target;if(t){const e=this.slottedRadioButtons;if(t.checked||e.indexOf(t)===0){t.setAttribute("tabindex","0");this.selectedRadio=t}else{t.setAttribute("tabindex","-1");this.selectedRadio=null}this.focusedRadio=t}e.preventDefault()};this.shouldMoveOffGroupToTheRight=(e,t,i)=>e===t.length&&this.isInsideToolbar&&i===si;this.shouldMoveOffGroupToTheLeft=(e,t)=>{const i=this.focusedRadio?e.indexOf(this.focusedRadio)-1:0;return i<0&&this.isInsideToolbar&&t===ii};this.checkFocusedRadio=()=>{if(this.focusedRadio!==null&&!this.focusedRadio.readOnly&&!this.focusedRadio.checked){this.focusedRadio.checked=true;this.focusedRadio.setAttribute("tabindex","0");this.focusedRadio.focus();this.selectedRadio=this.focusedRadio}};this.moveRight=e=>{const t=this.slottedRadioButtons;let i=0;i=this.focusedRadio?t.indexOf(this.focusedRadio)+1:1;if(this.shouldMoveOffGroupToTheRight(i,t,e.key)){this.moveRightOffGroup();return}else if(i===t.length){i=0}while(i<t.length&&t.length>1){if(!t[i].disabled){this.moveToRadioByIndex(t,i);break}else if(this.focusedRadio&&i===t.indexOf(this.focusedRadio)){break}else if(i+1>=t.length){if(this.isInsideToolbar){break}else{i=0}}else{i+=1}}};this.moveLeft=e=>{const t=this.slottedRadioButtons;let i=0;i=this.focusedRadio?t.indexOf(this.focusedRadio)-1:0;i=i<0?t.length-1:i;if(this.shouldMoveOffGroupToTheLeft(t,e.key)){this.moveLeftOffGroup();return}while(i>=0&&t.length>1){if(!t[i].disabled){this.moveToRadioByIndex(t,i);break}else if(this.focusedRadio&&i===t.indexOf(this.focusedRadio)){break}else if(i-1<0){i=t.length-1}else{i-=1}}};this.keydownHandler=e=>{const t=e.key;if(t in vi&&this.isInsideFoundationToolbar){return true}switch(t){case oi:{this.checkFocusedRadio();break}case si:case ti:{if(this.direction===Oi.N.ltr){this.moveRight(e)}else{this.moveLeft(e)}break}case ii:case ni:{if(this.direction===Oi.N.ltr){this.moveLeft(e)}else{this.moveRight(e)}break}default:{return true}}}}readOnlyChanged(){if(this.slottedRadioButtons!==undefined){this.slottedRadioButtons.forEach((e=>{if(this.readOnly){e.readOnly=true}else{e.readOnly=false}}))}}disabledChanged(){if(this.slottedRadioButtons!==undefined){this.slottedRadioButtons.forEach((e=>{if(this.disabled){e.disabled=true}else{e.disabled=false}}))}}nameChanged(){if(this.slottedRadioButtons){this.slottedRadioButtons.forEach((e=>{e.setAttribute("name",this.name)}))}}valueChanged(){if(this.slottedRadioButtons){this.slottedRadioButtons.forEach((e=>{if(e.value===this.value){e.checked=true;this.selectedRadio=e}}))}this.$emit("change")}slottedRadioButtonsChanged(e,t){if(this.slottedRadioButtons&&this.slottedRadioButtons.length>0){this.setupRadioButtons()}}get parentToolbar(){return this.closest('[role="toolbar"]')}get isInsideToolbar(){var e;return(e=this.parentToolbar)!==null&&e!==void 0?e:false}get isInsideFoundationToolbar(){var e;return!!((e=this.parentToolbar)===null||e===void 0?void 0:e["$fastController"])}connectedCallback(){super.connectedCallback();this.direction=no(this);this.setupRadioButtons()}disconnectedCallback(){this.slottedRadioButtons.forEach((e=>{e.removeEventListener("change",this.radioChangeHandler)}))}setupRadioButtons(){const e=this.slottedRadioButtons.filter((e=>e.hasAttribute("checked")));const t=e?e.length:0;if(t>1){const i=e[t-1];i.checked=true}let i=false;this.slottedRadioButtons.forEach((e=>{if(this.name!==undefined){e.setAttribute("name",this.name)}if(this.disabled){e.disabled=true}if(this.readOnly){e.readOnly=true}if(this.value&&this.value===e.value){this.selectedRadio=e;this.focusedRadio=e;e.checked=true;e.setAttribute("tabindex","0");i=true}else{if(!this.isInsideFoundationToolbar){e.setAttribute("tabindex","-1")}e.checked=false}e.addEventListener("change",this.radioChangeHandler)}));if(this.value===undefined&&this.slottedRadioButtons.length>0){const e=this.slottedRadioButtons.filter((e=>e.hasAttribute("checked")));const t=e!==null?e.length:0;if(t>0&&!i){const i=e[t-1];i.checked=true;this.focusedRadio=i;i.setAttribute("tabindex","0")}else{this.slottedRadioButtons[0].setAttribute("tabindex","0");this.focusedRadio=this.slottedRadioButtons[0]}}}}f([(0,s.attr)({attribute:"readonly",mode:"boolean"})],Gl.prototype,"readOnly",void 0);f([(0,s.attr)({attribute:"disabled",mode:"boolean"})],Gl.prototype,"disabled",void 0);f([s.attr],Gl.prototype,"name",void 0);f([s.attr],Gl.prototype,"value",void 0);f([s.attr],Gl.prototype,"orientation",void 0);f([s.observable],Gl.prototype,"childItems",void 0);f([s.observable],Gl.prototype,"slottedRadioButtons",void 0);const Yl=(e,t)=>s.html`
    <template
        role="radio"
        class="${e=>e.checked?"checked":""} ${e=>e.readOnly?"readonly":""}"
        aria-checked="${e=>e.checked}"
        aria-required="${e=>e.required}"
        aria-disabled="${e=>e.disabled}"
        aria-readonly="${e=>e.readOnly}"
        @keypress="${(e,t)=>e.keypressHandler(t.event)}"
        @click="${(e,t)=>e.clickHandler(t.event)}"
    >
        <div part="control" class="control">
            <slot name="checked-indicator">
                ${t.checkedIndicator||""}
            </slot>
        </div>
        <label
            part="label"
            class="${e=>e.defaultSlottedNodes&&e.defaultSlottedNodes.length?"label":"label label__hidden"}"
        >
            <slot ${(0,s.slotted)("defaultSlottedNodes")}></slot>
        </label>
    </template>
`;class Xl extends Fe{}class Ql extends(Ro(Xl)){constructor(){super(...arguments);this.proxy=document.createElement("input")}}class Zl extends Ql{constructor(){super();this.initialValue="on";this.keypressHandler=e=>{switch(e.key){case ui:if(!this.checked&&!this.readOnly){this.checked=true}return}return true};this.proxy.setAttribute("type","radio")}readOnlyChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.readOnly=this.readOnly}}defaultCheckedChanged(){var e;if(this.$fastController.isConnected&&!this.dirtyChecked){if(!this.isInsideRadioGroup()){this.checked=(e=this.defaultChecked)!==null&&e!==void 0?e:false;this.dirtyChecked=false}}}connectedCallback(){var e,t;super.connectedCallback();this.validate();if(((e=this.parentElement)===null||e===void 0?void 0:e.getAttribute("role"))!=="radiogroup"&&this.getAttribute("tabindex")===null){if(!this.disabled){this.setAttribute("tabindex","0")}}if(this.checkedAttribute){if(!this.dirtyChecked){if(!this.isInsideRadioGroup()){this.checked=(t=this.defaultChecked)!==null&&t!==void 0?t:false;this.dirtyChecked=false}}}}isInsideRadioGroup(){const e=this.closest("[role=radiogroup]");return e!==null}clickHandler(e){if(!this.disabled&&!this.readOnly&&!this.checked){this.checked=true}}}f([(0,s.attr)({attribute:"readonly",mode:"boolean"})],Zl.prototype,"readOnly",void 0);f([s.observable],Zl.prototype,"name",void 0);f([s.observable],Zl.prototype,"defaultSlottedNodes",void 0);class Jl extends Fe{constructor(){super(...arguments);this.framesPerSecond=60;this.updatingItems=false;this.speed=600;this.easing="ease-in-out";this.flippersHiddenFromAT=false;this.scrolling=false;this.resizeDetector=null}get frameTime(){return 1e3/this.framesPerSecond}scrollingChanged(e,t){if(this.scrollContainer){const e=this.scrolling==true?"scrollstart":"scrollend";this.$emit(e,this.scrollContainer.scrollLeft)}}get isRtl(){return this.scrollItems.length>1&&this.scrollItems[0].offsetLeft>this.scrollItems[1].offsetLeft}connectedCallback(){super.connectedCallback();this.initializeResizeDetector()}disconnectedCallback(){this.disconnectResizeDetector();super.disconnectedCallback()}scrollItemsChanged(e,t){if(t&&!this.updatingItems){s.DOM.queueUpdate((()=>this.setStops()))}}disconnectResizeDetector(){if(this.resizeDetector){this.resizeDetector.disconnect();this.resizeDetector=null}}initializeResizeDetector(){this.disconnectResizeDetector();this.resizeDetector=new window.ResizeObserver(this.resized.bind(this));this.resizeDetector.observe(this)}updateScrollStops(){this.updatingItems=true;const e=this.scrollItems.reduce(((e,t)=>{if(t instanceof HTMLSlotElement){return e.concat(t.assignedElements())}e.push(t);return e}),[]);this.scrollItems=e;this.updatingItems=false}setStops(){this.updateScrollStops();const{scrollContainer:e}=this;const{scrollLeft:t}=e;const{width:i,left:s}=e.getBoundingClientRect();this.width=i;let n=0;let o=this.scrollItems.map(((e,i)=>{const{left:o,width:r}=e.getBoundingClientRect();const a=Math.round(o+t-s);const l=Math.round(a+r);if(this.isRtl){return-l}n=l;return i===0?0:a})).concat(n);o=this.fixScrollMisalign(o);o.sort(((e,t)=>Math.abs(e)-Math.abs(t)));this.scrollStops=o;this.setFlippers()}validateStops(e=true){const t=()=>!!this.scrollStops.find((e=>e>0));if(!t()&&e){this.setStops()}return t()}fixScrollMisalign(e){if(this.isRtl&&e.some((e=>e>0))){e.sort(((e,t)=>t-e));const t=e[0];e=e.map((e=>e-t))}return e}setFlippers(){var e,t;const i=this.scrollContainer.scrollLeft;(e=this.previousFlipperContainer)===null||e===void 0?void 0:e.classList.toggle("disabled",i===0);if(this.scrollStops){const e=Math.abs(this.scrollStops[this.scrollStops.length-1]);(t=this.nextFlipperContainer)===null||t===void 0?void 0:t.classList.toggle("disabled",this.validateStops(false)&&Math.abs(i)+this.width>=e)}}scrollInView(e,t=0,i){var s;if(typeof e!=="number"&&e){e=this.scrollItems.findIndex((t=>t===e||t.contains(e)))}if(e!==undefined){i=i!==null&&i!==void 0?i:t;const{scrollContainer:n,scrollStops:o,scrollItems:r}=this;const{scrollLeft:a}=this.scrollContainer;const{width:l}=n.getBoundingClientRect();const d=o[e];const{width:h}=r[e].getBoundingClientRect();const c=d+h;const u=a+t>d;if(u||a+l-i<c){const e=[...o].sort(((e,t)=>u?t-e:e-t));const n=(s=e.find((e=>u?e+t<d:e+l-(i!==null&&i!==void 0?i:0)>c)))!==null&&s!==void 0?s:0;this.scrollToPosition(n)}}}keyupHandler(e){const t=e.key;switch(t){case"ArrowLeft":this.scrollToPrevious();break;case"ArrowRight":this.scrollToNext();break}}scrollToPrevious(){this.validateStops();const e=this.scrollContainer.scrollLeft;const t=this.scrollStops.findIndex(((t,i)=>t>=e&&(this.isRtl||i===this.scrollStops.length-1||this.scrollStops[i+1]>e)));const i=Math.abs(this.scrollStops[t+1]);let s=this.scrollStops.findIndex((e=>Math.abs(e)+this.width>i));if(s>=t||s===-1){s=t>0?t-1:0}this.scrollToPosition(this.scrollStops[s],e)}scrollToNext(){this.validateStops();const e=this.scrollContainer.scrollLeft;const t=this.scrollStops.findIndex((t=>Math.abs(t)>=Math.abs(e)));const i=this.scrollStops.findIndex((t=>Math.abs(e)+this.width<=Math.abs(t)));let s=t;if(i>t+2){s=i-2}else if(t<this.scrollStops.length-2){s=t+1}this.scrollToPosition(this.scrollStops[s],e)}scrollToPosition(e,t=this.scrollContainer.scrollLeft){var i;if(this.scrolling){return}this.scrolling=true;const s=(i=this.duration)!==null&&i!==void 0?i:`${Math.abs(e-t)/this.speed}s`;this.content.style.setProperty("transition-duration",s);const n=parseFloat(getComputedStyle(this.content).getPropertyValue("transition-duration"));const o=t=>{if(t&&t.target!==t.currentTarget){return}this.content.style.setProperty("transition-duration","0s");this.content.style.removeProperty("transform");this.scrollContainer.style.setProperty("scroll-behavior","auto");this.scrollContainer.scrollLeft=e;this.setFlippers();this.content.removeEventListener("transitionend",o);this.scrolling=false};if(n===0){o();return}this.content.addEventListener("transitionend",o);const r=this.scrollContainer.scrollWidth-this.scrollContainer.clientWidth;let a=this.scrollContainer.scrollLeft-Math.min(e,r);if(this.isRtl){a=this.scrollContainer.scrollLeft+Math.min(Math.abs(e),r)}this.content.style.setProperty("transition-property","transform");this.content.style.setProperty("transition-timing-function",this.easing);this.content.style.setProperty("transform",`translateX(${a}px)`)}resized(){if(this.resizeTimeout){this.resizeTimeout=clearTimeout(this.resizeTimeout)}this.resizeTimeout=setTimeout((()=>{this.width=this.scrollContainer.offsetWidth;this.setFlippers()}),this.frameTime)}scrolled(){if(this.scrollTimeout){this.scrollTimeout=clearTimeout(this.scrollTimeout)}this.scrollTimeout=setTimeout((()=>{this.setFlippers()}),this.frameTime)}}f([(0,s.attr)({converter:s.nullableNumberConverter})],Jl.prototype,"speed",void 0);f([s.attr],Jl.prototype,"duration",void 0);f([s.attr],Jl.prototype,"easing",void 0);f([(0,s.attr)({attribute:"flippers-hidden-from-at",converter:s.booleanConverter})],Jl.prototype,"flippersHiddenFromAT",void 0);f([s.observable],Jl.prototype,"scrolling",void 0);f([s.observable],Jl.prototype,"scrollItems",void 0);f([(0,s.attr)({attribute:"view"})],Jl.prototype,"view",void 0);const ed=(e,t)=>{var i,n;return s.html`
    <template
        class="horizontal-scroll"
        @keyup="${(e,t)=>e.keyupHandler(t.event)}"
    >
        ${r(e,t)}
        <div class="scroll-area" part="scroll-area">
            <div
                class="scroll-view"
                part="scroll-view"
                @scroll="${e=>e.scrolled()}"
                ${(0,s.ref)("scrollContainer")}
            >
                <div class="content-container" part="content-container" ${(0,s.ref)("content")}>
                    <slot
                        ${(0,s.slotted)({property:"scrollItems",filter:(0,s.elements)()})}
                    ></slot>
                </div>
            </div>
            ${(0,s.when)((e=>e.view!=="mobile"),s.html`
                    <div
                        class="scroll scroll-prev"
                        part="scroll-prev"
                        ${(0,s.ref)("previousFlipperContainer")}
                    >
                        <div class="scroll-action" part="scroll-action-previous">
                            <slot name="previous-flipper">
                                ${t.previousFlipper instanceof Function?t.previousFlipper(e,t):(i=t.previousFlipper)!==null&&i!==void 0?i:""}
                            </slot>
                        </div>
                    </div>
                    <div
                        class="scroll scroll-next"
                        part="scroll-next"
                        ${(0,s.ref)("nextFlipperContainer")}
                    >
                        <div class="scroll-action" part="scroll-action-next">
                            <slot name="next-flipper">
                                ${t.nextFlipper instanceof Function?t.nextFlipper(e,t):(n=t.nextFlipper)!==null&&n!==void 0?n:""}
                            </slot>
                        </div>
                    </div>
                `)}
        </div>
        ${o(e,t)}
    </template>
`};function td(e,t,i){return e.nodeType!==Node.TEXT_NODE?true:typeof e.nodeValue==="string"&&!!e.nodeValue.trim().length}const id=(e,t)=>s.html`
    <template
        class="
            ${e=>e.readOnly?"readonly":""}
        "
    >
        <label
            part="label"
            for="control"
            class="${e=>e.defaultSlottedNodes&&e.defaultSlottedNodes.length?"label":"label label__hidden"}"
        >
            <slot
                ${(0,s.slotted)({property:"defaultSlottedNodes",filter:td})}
            ></slot>
        </label>
        <div class="root" part="root" ${(0,s.ref)("root")}>
            ${r(e,t)}
            <div class="input-wrapper" part="input-wrapper">
                <input
                    class="control"
                    part="control"
                    id="control"
                    @input="${e=>e.handleTextInput()}"
                    @change="${e=>e.handleChange()}"
                    ?autofocus="${e=>e.autofocus}"
                    ?disabled="${e=>e.disabled}"
                    list="${e=>e.list}"
                    maxlength="${e=>e.maxlength}"
                    minlength="${e=>e.minlength}"
                    pattern="${e=>e.pattern}"
                    placeholder="${e=>e.placeholder}"
                    ?readonly="${e=>e.readOnly}"
                    ?required="${e=>e.required}"
                    size="${e=>e.size}"
                    ?spellcheck="${e=>e.spellcheck}"
                    :value="${e=>e.value}"
                    type="search"
                    aria-atomic="${e=>e.ariaAtomic}"
                    aria-busy="${e=>e.ariaBusy}"
                    aria-controls="${e=>e.ariaControls}"
                    aria-current="${e=>e.ariaCurrent}"
                    aria-describedby="${e=>e.ariaDescribedby}"
                    aria-details="${e=>e.ariaDetails}"
                    aria-disabled="${e=>e.ariaDisabled}"
                    aria-errormessage="${e=>e.ariaErrormessage}"
                    aria-flowto="${e=>e.ariaFlowto}"
                    aria-haspopup="${e=>e.ariaHaspopup}"
                    aria-hidden="${e=>e.ariaHidden}"
                    aria-invalid="${e=>e.ariaInvalid}"
                    aria-keyshortcuts="${e=>e.ariaKeyshortcuts}"
                    aria-label="${e=>e.ariaLabel}"
                    aria-labelledby="${e=>e.ariaLabelledby}"
                    aria-live="${e=>e.ariaLive}"
                    aria-owns="${e=>e.ariaOwns}"
                    aria-relevant="${e=>e.ariaRelevant}"
                    aria-roledescription="${e=>e.ariaRoledescription}"
                    ${(0,s.ref)("control")}
                />
                <slot name="close-button">
                    <button
                        class="clear-button ${e=>e.value?"":"clear-button__hidden"}"
                        part="clear-button"
                        tabindex="-1"
                        @click=${e=>e.handleClearInput()}
                    >
                        <slot name="close-glyph">
                            <svg
                                width="9"
                                height="9"
                                viewBox="0 0 9 9"
                                xmlns="http://www.w3.org/2000/svg"
                            >
                                <path
                                    d="M0.146447 0.146447C0.338683 -0.0478972 0.645911 -0.0270359 0.853553 0.146447L4.5 3.793L8.14645 0.146447C8.34171 -0.0488155 8.65829 -0.0488155 8.85355 0.146447C9.04882 0.341709 9.04882 0.658291 8.85355 0.853553L5.207 4.5L8.85355 8.14645C9.05934 8.35223 9.03129 8.67582 8.85355 8.85355C8.67582 9.03129 8.35409 9.02703 8.14645 8.85355L4.5 5.207L0.853553 8.85355C0.658291 9.04882 0.341709 9.04882 0.146447 8.85355C-0.0488155 8.65829 -0.0488155 8.34171 0.146447 8.14645L3.793 4.5L0.146447 0.853553C-0.0268697 0.680237 -0.0457894 0.34079 0.146447 0.146447Z"
                                />
                            </svg>
                        </slot>
                    </button>
                </slot>
            </div>
            ${o(e,t)}
        </div>
    </template>
`;class sd extends Fe{}class nd extends(To(sd)){constructor(){super(...arguments);this.proxy=document.createElement("input")}}class od extends nd{readOnlyChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.readOnly=this.readOnly;this.validate()}}autofocusChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.autofocus=this.autofocus;this.validate()}}placeholderChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.placeholder=this.placeholder}}listChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.setAttribute("list",this.list);this.validate()}}maxlengthChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.maxLength=this.maxlength;this.validate()}}minlengthChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.minLength=this.minlength;this.validate()}}patternChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.pattern=this.pattern;this.validate()}}sizeChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.size=this.size}}spellcheckChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.spellcheck=this.spellcheck}}connectedCallback(){super.connectedCallback();this.validate();if(this.autofocus){s.DOM.queueUpdate((()=>{this.focus()}))}}validate(){super.validate(this.control)}handleTextInput(){this.value=this.control.value}handleClearInput(){this.value="";this.control.focus();this.handleChange()}handleChange(){this.$emit("change")}}f([(0,s.attr)({attribute:"readonly",mode:"boolean"})],od.prototype,"readOnly",void 0);f([(0,s.attr)({mode:"boolean"})],od.prototype,"autofocus",void 0);f([s.attr],od.prototype,"placeholder",void 0);f([s.attr],od.prototype,"list",void 0);f([(0,s.attr)({converter:s.nullableNumberConverter})],od.prototype,"maxlength",void 0);f([(0,s.attr)({converter:s.nullableNumberConverter})],od.prototype,"minlength",void 0);f([s.attr],od.prototype,"pattern",void 0);f([(0,s.attr)({converter:s.nullableNumberConverter})],od.prototype,"size",void 0);f([(0,s.attr)({mode:"boolean"})],od.prototype,"spellcheck",void 0);f([s.observable],od.prototype,"defaultSlottedNodes",void 0);class rd{}Me(rd,$i);Me(od,n,rd);class ad extends dl{}class ld extends(To(ad)){constructor(){super(...arguments);this.proxy=document.createElement("select")}}class dd extends ld{constructor(){super(...arguments);this.open=false;this.forcedPosition=false;this.listboxId=nr("listbox-");this.maxHeight=0}openChanged(e,t){if(!this.collapsible){return}if(this.open){this.ariaControls=this.listboxId;this.ariaExpanded="true";this.setPositioning();this.focusAndScrollOptionIntoView();this.indexWhenOpened=this.selectedIndex;s.DOM.queueUpdate((()=>this.focus()));return}this.ariaControls="";this.ariaExpanded="false"}get collapsible(){return!(this.multiple||typeof this.size==="number")}get value(){s.Observable.track(this,"value");return this._value}set value(e){var t,i,n,o,r,a,l;const d=`${this._value}`;if((t=this._options)===null||t===void 0?void 0:t.length){const t=this._options.findIndex((t=>t.value===e));const s=(n=(i=this._options[this.selectedIndex])===null||i===void 0?void 0:i.value)!==null&&n!==void 0?n:null;const d=(r=(o=this._options[t])===null||o===void 0?void 0:o.value)!==null&&r!==void 0?r:null;if(t===-1||s!==d){e="";this.selectedIndex=t}e=(l=(a=this.firstSelectedOption)===null||a===void 0?void 0:a.value)!==null&&l!==void 0?l:e}if(d!==e){this._value=e;super.valueChanged(d,e);s.Observable.notify(this,"value");this.updateDisplayValue()}}updateValue(e){var t,i;if(this.$fastController.isConnected){this.value=(i=(t=this.firstSelectedOption)===null||t===void 0?void 0:t.value)!==null&&i!==void 0?i:""}if(e){this.$emit("input");this.$emit("change",this,{bubbles:true,composed:undefined})}}selectedIndexChanged(e,t){super.selectedIndexChanged(e,t);this.updateValue()}positionChanged(e,t){this.positionAttribute=t;this.setPositioning()}setPositioning(){const e=this.getBoundingClientRect();const t=window.innerHeight;const i=t-e.bottom;this.position=this.forcedPosition?this.positionAttribute:e.top>i?Tr.above:Tr.below;this.positionAttribute=this.forcedPosition?this.positionAttribute:this.position;this.maxHeight=this.position===Tr.above?~~e.top:~~i}get displayValue(){var e,t;s.Observable.track(this,"displayValue");return(t=(e=this.firstSelectedOption)===null||e===void 0?void 0:e.text)!==null&&t!==void 0?t:""}disabledChanged(e,t){if(super.disabledChanged){super.disabledChanged(e,t)}this.ariaDisabled=this.disabled?"true":"false"}formResetCallback(){this.setProxyOptions();super.setDefaultSelectedOption();if(this.selectedIndex===-1){this.selectedIndex=0}}clickHandler(e){if(this.disabled){return}if(this.open){const t=e.target.closest(`option,[role=option]`);if(t&&t.disabled){return}}super.clickHandler(e);this.open=this.collapsible&&!this.open;if(!this.open&&this.indexWhenOpened!==this.selectedIndex){this.updateValue(true)}return true}focusoutHandler(e){var t;super.focusoutHandler(e);if(!this.open){return true}const i=e.relatedTarget;if(this.isSameNode(i)){this.focus();return}if(!((t=this.options)===null||t===void 0?void 0:t.includes(i))){this.open=false;if(this.indexWhenOpened!==this.selectedIndex){this.updateValue(true)}}}handleChange(e,t){super.handleChange(e,t);if(t==="value"){this.updateValue()}}slottedOptionsChanged(e,t){this.options.forEach((e=>{const t=s.Observable.getNotifier(e);t.unsubscribe(this,"value")}));super.slottedOptionsChanged(e,t);this.options.forEach((e=>{const t=s.Observable.getNotifier(e);t.subscribe(this,"value")}));this.setProxyOptions();this.updateValue()}mousedownHandler(e){var t;if(e.offsetX>=0&&e.offsetX<=((t=this.listbox)===null||t===void 0?void 0:t.scrollWidth)){return super.mousedownHandler(e)}return this.collapsible}multipleChanged(e,t){super.multipleChanged(e,t);if(this.proxy){this.proxy.multiple=t}}selectedOptionsChanged(e,t){var i;super.selectedOptionsChanged(e,t);(i=this.options)===null||i===void 0?void 0:i.forEach(((e,t)=>{var i;const s=(i=this.proxy)===null||i===void 0?void 0:i.options.item(t);if(s){s.selected=e.selected}}))}setDefaultSelectedOption(){var e;const t=(e=this.options)!==null&&e!==void 0?e:Array.from(this.children).filter(Er.slottedOptionFilter);const i=t===null||t===void 0?void 0:t.findIndex((e=>e.hasAttribute("selected")||e.selected||e.value===this.value));if(i!==-1){this.selectedIndex=i;return}this.selectedIndex=0}setProxyOptions(){if(this.proxy instanceof HTMLSelectElement&&this.options){this.proxy.options.length=0;this.options.forEach((e=>{const t=e.proxy||(e instanceof HTMLOptionElement?e.cloneNode():null);if(t){this.proxy.options.add(t)}}))}}keydownHandler(e){super.keydownHandler(e);const t=e.key||e.key.charCodeAt(0);switch(t){case ui:{e.preventDefault();if(this.collapsible&&this.typeAheadExpired){this.open=!this.open}break}case ai:case li:{e.preventDefault();break}case oi:{e.preventDefault();this.open=!this.open;break}case ri:{if(this.collapsible&&this.open){e.preventDefault();this.open=false}break}case pi:{if(this.collapsible&&this.open){e.preventDefault();this.open=false}return true}}if(!this.open&&this.indexWhenOpened!==this.selectedIndex){this.updateValue(true);this.indexWhenOpened=this.selectedIndex}return!(t===ti||t===ni)}connectedCallback(){super.connectedCallback();this.forcedPosition=!!this.positionAttribute;this.addEventListener("contentchange",this.updateDisplayValue)}disconnectedCallback(){this.removeEventListener("contentchange",this.updateDisplayValue);super.disconnectedCallback()}sizeChanged(e,t){super.sizeChanged(e,t);if(this.proxy){this.proxy.size=t}}updateDisplayValue(){if(this.collapsible){s.Observable.notify(this,"displayValue")}}}f([(0,s.attr)({attribute:"open",mode:"boolean"})],dd.prototype,"open",void 0);f([s.volatile],dd.prototype,"collapsible",null);f([s.observable],dd.prototype,"control",void 0);f([(0,s.attr)({attribute:"position"})],dd.prototype,"positionAttribute",void 0);f([s.observable],dd.prototype,"position",void 0);f([s.observable],dd.prototype,"maxHeight",void 0);class hd{}f([s.observable],hd.prototype,"ariaControls",void 0);Me(hd,Or);Me(dd,n,hd);const cd=(e,t)=>s.html`
    <template
        class="${e=>[e.collapsible&&"collapsible",e.collapsible&&e.open&&"open",e.disabled&&"disabled",e.collapsible&&e.position].filter(Boolean).join(" ")}"
        aria-activedescendant="${e=>e.ariaActiveDescendant}"
        aria-controls="${e=>e.ariaControls}"
        aria-disabled="${e=>e.ariaDisabled}"
        aria-expanded="${e=>e.ariaExpanded}"
        aria-haspopup="${e=>e.collapsible?"listbox":null}"
        aria-multiselectable="${e=>e.ariaMultiSelectable}"
        ?open="${e=>e.open}"
        role="combobox"
        tabindex="${e=>!e.disabled?"0":null}"
        @click="${(e,t)=>e.clickHandler(t.event)}"
        @focusin="${(e,t)=>e.focusinHandler(t.event)}"
        @focusout="${(e,t)=>e.focusoutHandler(t.event)}"
        @keydown="${(e,t)=>e.keydownHandler(t.event)}"
        @mousedown="${(e,t)=>e.mousedownHandler(t.event)}"
    >
        ${(0,s.when)((e=>e.collapsible),s.html`
                <div
                    class="control"
                    part="control"
                    ?disabled="${e=>e.disabled}"
                    ${(0,s.ref)("control")}
                >
                    ${r(e,t)}
                    <slot name="button-container">
                        <div class="selected-value" part="selected-value">
                            <slot name="selected-value">${e=>e.displayValue}</slot>
                        </div>
                        <div aria-hidden="true" class="indicator" part="indicator">
                            <slot name="indicator">
                                ${t.indicator||""}
                            </slot>
                        </div>
                    </slot>
                    ${o(e,t)}
                </div>
            `)}
        <div
            class="listbox"
            id="${e=>e.listboxId}"
            part="listbox"
            role="listbox"
            ?disabled="${e=>e.disabled}"
            ?hidden="${e=>e.collapsible?!e.open:false}"
            ${(0,s.ref)("listbox")}
        >
            <slot
                ${(0,s.slotted)({filter:Er.slottedOptionFilter,flatten:true,property:"slottedOptions"})}
            ></slot>
        </div>
    </template>
`;const ud=(e,t)=>s.html`
    <template
        class="${e=>e.shape==="circle"?"circle":"rect"}"
        pattern="${e=>e.pattern}"
        ?shimmer="${e=>e.shimmer}"
    >
        ${(0,s.when)((e=>e.shimmer===true),s.html`
                <span class="shimmer"></span>
            `)}
        <object type="image/svg+xml" data="${e=>e.pattern}" role="presentation">
            <img class="pattern" src="${e=>e.pattern}" />
        </object>
        <slot></slot>
    </template>
`;class pd extends Fe{constructor(){super(...arguments);this.shape="rect"}}f([s.attr],pd.prototype,"fill",void 0);f([s.attr],pd.prototype,"shape",void 0);f([s.attr],pd.prototype,"pattern",void 0);f([(0,s.attr)({mode:"boolean"})],pd.prototype,"shimmer",void 0);const fd=(e,t)=>s.html`
    <template
        aria-disabled="${e=>e.disabled}"
        class="${e=>e.sliderOrientation||il.i.horizontal}
            ${e=>e.disabled?"disabled":""}"
    >
        <div ${(0,s.ref)("root")} part="root" class="root" style="${e=>e.positionStyle}">
            <div class="container">
                ${(0,s.when)((e=>!e.hideMark),s.html`
                        <div class="mark"></div>
                    `)}
                <div class="label">
                    <slot></slot>
                </div>
            </div>
        </div>
    </template>
`;function md(e,t,i,s){let n=gi(0,1,(e-t)/(i-t));if(s===Oi.N.rtl){n=1-n}return n}const vd={min:0,max:0,direction:Oi.N.ltr,orientation:il.i.horizontal,disabled:false};class bd extends Fe{constructor(){super(...arguments);this.hideMark=false;this.sliderDirection=Oi.N.ltr;this.getSliderConfiguration=()=>{if(!this.isSliderConfig(this.parentNode)){this.sliderDirection=vd.direction||Oi.N.ltr;this.sliderOrientation=vd.orientation||il.i.horizontal;this.sliderMaxPosition=vd.max;this.sliderMinPosition=vd.min}else{const e=this.parentNode;const{min:t,max:i,direction:s,orientation:n,disabled:o}=e;if(o!==undefined){this.disabled=o}this.sliderDirection=s||Oi.N.ltr;this.sliderOrientation=n||il.i.horizontal;this.sliderMaxPosition=i;this.sliderMinPosition=t}};this.positionAsStyle=()=>{const e=this.sliderDirection?this.sliderDirection:Oi.N.ltr;const t=md(Number(this.position),Number(this.sliderMinPosition),Number(this.sliderMaxPosition));let i=Math.round((1-t)*100);let s=Math.round(t*100);if(Number.isNaN(s)&&Number.isNaN(i)){i=50;s=50}if(this.sliderOrientation===il.i.horizontal){return e===Oi.N.rtl?`right: ${s}%; left: ${i}%;`:`left: ${s}%; right: ${i}%;`}else{return`top: ${s}%; bottom: ${i}%;`}}}positionChanged(){this.positionStyle=this.positionAsStyle()}sliderOrientationChanged(){void 0}connectedCallback(){super.connectedCallback();this.getSliderConfiguration();this.positionStyle=this.positionAsStyle();this.notifier=s.Observable.getNotifier(this.parentNode);this.notifier.subscribe(this,"orientation");this.notifier.subscribe(this,"direction");this.notifier.subscribe(this,"max");this.notifier.subscribe(this,"min")}disconnectedCallback(){super.disconnectedCallback();this.notifier.unsubscribe(this,"orientation");this.notifier.unsubscribe(this,"direction");this.notifier.unsubscribe(this,"max");this.notifier.unsubscribe(this,"min")}handleChange(e,t){switch(t){case"direction":this.sliderDirection=e.direction;break;case"orientation":this.sliderOrientation=e.orientation;break;case"max":this.sliderMaxPosition=e.max;break;case"min":this.sliderMinPosition=e.min;break;default:break}this.positionStyle=this.positionAsStyle()}isSliderConfig(e){return e.max!==undefined&&e.min!==undefined}}f([s.observable],bd.prototype,"positionStyle",void 0);f([s.attr],bd.prototype,"position",void 0);f([(0,s.attr)({attribute:"hide-mark",mode:"boolean"})],bd.prototype,"hideMark",void 0);f([(0,s.attr)({attribute:"disabled",mode:"boolean"})],bd.prototype,"disabled",void 0);f([s.observable],bd.prototype,"sliderOrientation",void 0);f([s.observable],bd.prototype,"sliderMinPosition",void 0);f([s.observable],bd.prototype,"sliderMaxPosition",void 0);f([s.observable],bd.prototype,"sliderDirection",void 0);const gd=(e,t)=>s.html`
    <template
        role="slider"
        class="${e=>e.readOnly?"readonly":""}
        ${e=>e.orientation||il.i.horizontal}"
        tabindex="${e=>e.disabled?null:0}"
        aria-valuetext="${e=>e.valueTextFormatter(e.value)}"
        aria-valuenow="${e=>e.value}"
        aria-valuemin="${e=>e.min}"
        aria-valuemax="${e=>e.max}"
        aria-disabled="${e=>e.disabled?true:void 0}"
        aria-readonly="${e=>e.readOnly?true:void 0}"
        aria-orientation="${e=>e.orientation}"
        class="${e=>e.orientation}"
    >
        <div part="positioning-region" class="positioning-region">
            <div ${(0,s.ref)("track")} part="track-container" class="track">
                <slot name="track"></slot>
                <div part="track-start" class="track-start" style="${e=>e.position}">
                    <slot name="track-start"></slot>
                </div>
            </div>
            <slot></slot>
            <div
                ${(0,s.ref)("thumb")}
                part="thumb-container"
                class="thumb-container"
                style="${e=>e.position}"
            >
                <slot name="thumb">${t.thumb||""}</slot>
            </div>
        </div>
    </template>
`;class yd extends Fe{}class Cd extends(To(yd)){constructor(){super(...arguments);this.proxy=document.createElement("input")}}const xd={singleValue:"single-value"};class wd extends Cd{constructor(){super(...arguments);this.direction=Oi.N.ltr;this.isDragging=false;this.trackWidth=0;this.trackMinWidth=0;this.trackHeight=0;this.trackLeft=0;this.trackMinHeight=0;this.valueTextFormatter=()=>null;this.min=0;this.max=10;this.step=1;this.orientation=il.i.horizontal;this.mode=xd.singleValue;this.keypressHandler=e=>{if(this.readOnly){return}if(e.key===ai){e.preventDefault();this.value=`${this.min}`}else if(e.key===li){e.preventDefault();this.value=`${this.max}`}else if(!e.shiftKey){switch(e.key){case si:case ni:e.preventDefault();this.increment();break;case ii:case ti:e.preventDefault();this.decrement();break}}};this.setupTrackConstraints=()=>{const e=this.track.getBoundingClientRect();this.trackWidth=this.track.clientWidth;this.trackMinWidth=this.track.clientLeft;this.trackHeight=e.bottom;this.trackMinHeight=e.top;this.trackLeft=this.getBoundingClientRect().left;if(this.trackWidth===0){this.trackWidth=1}};this.setupListeners=(e=false)=>{const t=`${e?"remove":"add"}EventListener`;this[t]("keydown",this.keypressHandler);this[t]("mousedown",this.handleMouseDown);this.thumb[t]("mousedown",this.handleThumbMouseDown,{passive:true});this.thumb[t]("touchstart",this.handleThumbMouseDown,{passive:true});if(e){this.handleMouseDown(null);this.handleThumbMouseDown(null)}};this.initialValue="";this.handleThumbMouseDown=e=>{if(e){if(this.readOnly||this.disabled||e.defaultPrevented){return}e.target.focus()}const t=`${e!==null?"add":"remove"}EventListener`;window[t]("mouseup",this.handleWindowMouseUp);window[t]("mousemove",this.handleMouseMove,{passive:true});window[t]("touchmove",this.handleMouseMove,{passive:true});window[t]("touchend",this.handleWindowMouseUp);this.isDragging=e!==null};this.handleMouseMove=e=>{if(this.readOnly||this.disabled||e.defaultPrevented){return}const t=window.TouchEvent&&e instanceof TouchEvent?e.touches[0]:e;const i=this.orientation===il.i.horizontal?t.pageX-document.documentElement.scrollLeft-this.trackLeft:t.pageY-document.documentElement.scrollTop;this.value=`${this.calculateNewValue(i)}`};this.calculateNewValue=e=>{const t=md(e,this.orientation===il.i.horizontal?this.trackMinWidth:this.trackMinHeight,this.orientation===il.i.horizontal?this.trackWidth:this.trackHeight,this.direction);const i=(this.max-this.min)*t+this.min;return this.convertToConstrainedValue(i)};this.handleWindowMouseUp=e=>{this.stopDragging()};this.stopDragging=()=>{this.isDragging=false;this.handleMouseDown(null);this.handleThumbMouseDown(null)};this.handleMouseDown=e=>{const t=`${e!==null?"add":"remove"}EventListener`;if(e===null||!this.disabled&&!this.readOnly){window[t]("mouseup",this.handleWindowMouseUp);window.document[t]("mouseleave",this.handleWindowMouseUp);window[t]("mousemove",this.handleMouseMove);if(e){e.preventDefault();this.setupTrackConstraints();e.target.focus();const t=this.orientation===il.i.horizontal?e.pageX-document.documentElement.scrollLeft-this.trackLeft:e.pageY-document.documentElement.scrollTop;this.value=`${this.calculateNewValue(t)}`}}};this.convertToConstrainedValue=e=>{if(isNaN(e)){e=this.min}let t=e-this.min;const i=Math.round(t/this.step);const s=t-i*(this.stepMultiplier*this.step)/this.stepMultiplier;t=s>=Number(this.step)/2?t-s+Number(this.step):t-s;return t+this.min}}readOnlyChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.readOnly=this.readOnly}}get valueAsNumber(){return parseFloat(super.value)}set valueAsNumber(e){this.value=e.toString()}valueChanged(e,t){super.valueChanged(e,t);if(this.$fastController.isConnected){this.setThumbPositionForOrientation(this.direction)}this.$emit("change")}minChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.min=`${this.min}`}this.validate()}maxChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.max=`${this.max}`}this.validate()}stepChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.step=`${this.step}`}this.updateStepMultiplier();this.validate()}orientationChanged(){if(this.$fastController.isConnected){this.setThumbPositionForOrientation(this.direction)}}connectedCallback(){super.connectedCallback();this.proxy.setAttribute("type","range");this.direction=no(this);this.updateStepMultiplier();this.setupTrackConstraints();this.setupListeners();this.setupDefaultValue();this.setThumbPositionForOrientation(this.direction)}disconnectedCallback(){this.setupListeners(true)}increment(){const e=this.direction!==Oi.N.rtl&&this.orientation!==il.i.vertical?Number(this.value)+Number(this.step):Number(this.value)-Number(this.step);const t=this.convertToConstrainedValue(e);const i=t<Number(this.max)?`${t}`:`${this.max}`;this.value=i}decrement(){const e=this.direction!==Oi.N.rtl&&this.orientation!==il.i.vertical?Number(this.value)-Number(this.step):Number(this.value)+Number(this.step);const t=this.convertToConstrainedValue(e);const i=t>Number(this.min)?`${t}`:`${this.min}`;this.value=i}setThumbPositionForOrientation(e){const t=md(Number(this.value),Number(this.min),Number(this.max),e);const i=(1-t)*100;if(this.orientation===il.i.horizontal){this.position=this.isDragging?`right: ${i}%; transition: none;`:`right: ${i}%; transition: all 0.2s ease;`}else{this.position=this.isDragging?`bottom: ${i}%; transition: none;`:`bottom: ${i}%; transition: all 0.2s ease;`}}updateStepMultiplier(){const e=this.step+"";const t=!!(this.step%1)?e.length-e.indexOf(".")-1:0;this.stepMultiplier=Math.pow(10,t)}get midpoint(){return`${this.convertToConstrainedValue((this.max+this.min)/2)}`}setupDefaultValue(){if(typeof this.value==="string"){if(this.value.length===0){this.initialValue=this.midpoint}else{const e=parseFloat(this.value);if(!Number.isNaN(e)&&(e<this.min||e>this.max)){this.value=this.midpoint}}}}}f([(0,s.attr)({attribute:"readonly",mode:"boolean"})],wd.prototype,"readOnly",void 0);f([s.observable],wd.prototype,"direction",void 0);f([s.observable],wd.prototype,"isDragging",void 0);f([s.observable],wd.prototype,"position",void 0);f([s.observable],wd.prototype,"trackWidth",void 0);f([s.observable],wd.prototype,"trackMinWidth",void 0);f([s.observable],wd.prototype,"trackHeight",void 0);f([s.observable],wd.prototype,"trackLeft",void 0);f([s.observable],wd.prototype,"trackMinHeight",void 0);f([s.observable],wd.prototype,"valueTextFormatter",void 0);f([(0,s.attr)({converter:s.nullableNumberConverter})],wd.prototype,"min",void 0);f([(0,s.attr)({converter:s.nullableNumberConverter})],wd.prototype,"max",void 0);f([(0,s.attr)({converter:s.nullableNumberConverter})],wd.prototype,"step",void 0);f([s.attr],wd.prototype,"orientation",void 0);f([s.attr],wd.prototype,"mode",void 0);const $d=(e,t)=>s.html`
    <template
        role="switch"
        aria-checked="${e=>e.checked}"
        aria-disabled="${e=>e.disabled}"
        aria-readonly="${e=>e.readOnly}"
        tabindex="${e=>e.disabled?null:0}"
        @keypress="${(e,t)=>e.keypressHandler(t.event)}"
        @click="${(e,t)=>e.clickHandler(t.event)}"
        class="${e=>e.checked?"checked":""}"
    >
        <label
            part="label"
            class="${e=>e.defaultSlottedNodes&&e.defaultSlottedNodes.length?"label":"label label__hidden"}"
        >
            <slot ${(0,s.slotted)("defaultSlottedNodes")}></slot>
        </label>
        <div part="switch" class="switch">
            <slot name="switch">${t.switch||""}</slot>
        </div>
        <span class="status-message" part="status-message">
            <span class="checked-message" part="checked-message">
                <slot name="checked-message"></slot>
            </span>
            <span class="unchecked-message" part="unchecked-message">
                <slot name="unchecked-message"></slot>
            </span>
        </span>
    </template>
`;class kd extends Fe{}class Id extends(Ro(kd)){constructor(){super(...arguments);this.proxy=document.createElement("input")}}class Ed extends Id{constructor(){super();this.initialValue="on";this.keypressHandler=e=>{if(this.readOnly){return}switch(e.key){case oi:case ui:this.checked=!this.checked;break}};this.clickHandler=e=>{if(!this.disabled&&!this.readOnly){this.checked=!this.checked}};this.proxy.setAttribute("type","checkbox")}readOnlyChanged(){if(this.proxy instanceof HTMLInputElement){this.proxy.readOnly=this.readOnly}this.readOnly?this.classList.add("readonly"):this.classList.remove("readonly")}checkedChanged(e,t){super.checkedChanged(e,t);this.checked?this.classList.add("checked"):this.classList.remove("checked")}}f([(0,s.attr)({attribute:"readonly",mode:"boolean"})],Ed.prototype,"readOnly",void 0);f([s.observable],Ed.prototype,"defaultSlottedNodes",void 0);const Od=(e,t)=>s.html`
    <template slot="tabpanel" role="tabpanel">
        <slot></slot>
    </template>
`;class Td extends Fe{}const Rd=(e,t)=>s.html`
    <template slot="tab" role="tab" aria-disabled="${e=>e.disabled}">
        <slot></slot>
    </template>
`;class Sd extends Fe{}f([(0,s.attr)({mode:"boolean"})],Sd.prototype,"disabled",void 0);const Dd=(e,t)=>s.html`
    <template class="${e=>e.orientation}">
        ${r(e,t)}
        <div class="tablist" part="tablist" role="tablist">
            <slot class="tab" name="tab" part="tab" ${(0,s.slotted)("tabs")}></slot>

            ${(0,s.when)((e=>e.showActiveIndicator),s.html`
                    <div
                        ${(0,s.ref)("activeIndicatorRef")}
                        class="activeIndicator"
                        part="activeIndicator"
                    ></div>
                `)}
        </div>
        ${o(e,t)}
        <div class="tabpanel" part="tabpanel">
            <slot name="tabpanel" ${(0,s.slotted)("tabpanels")}></slot>
        </div>
    </template>
`;const Ad={vertical:"vertical",horizontal:"horizontal"};class Fd extends Fe{constructor(){super(...arguments);this.orientation=Ad.horizontal;this.activeindicator=true;this.showActiveIndicator=true;this.prevActiveTabIndex=0;this.activeTabIndex=0;this.ticking=false;this.change=()=>{this.$emit("change",this.activetab)};this.isDisabledElement=e=>e.getAttribute("aria-disabled")==="true";this.isHiddenElement=e=>e.hasAttribute("hidden");this.isFocusableElement=e=>!this.isDisabledElement(e)&&!this.isHiddenElement(e);this.setTabs=()=>{const e="gridColumn";const t="gridRow";const i=this.isHorizontal()?e:t;this.activeTabIndex=this.getActiveIndex();this.showActiveIndicator=false;this.tabs.forEach(((s,n)=>{if(s.slot==="tab"){const e=this.activeTabIndex===n&&this.isFocusableElement(s);if(this.activeindicator&&this.isFocusableElement(s)){this.showActiveIndicator=true}const t=this.tabIds[n];const i=this.tabpanelIds[n];s.setAttribute("id",t);s.setAttribute("aria-selected",e?"true":"false");s.setAttribute("aria-controls",i);s.addEventListener("click",this.handleTabClick);s.addEventListener("keydown",this.handleTabKeyDown);s.setAttribute("tabindex",e?"0":"-1");if(e){this.activetab=s;this.activeid=t}}s.style[e]="";s.style[t]="";s.style[i]=`${n+1}`;!this.isHorizontal()?s.classList.add("vertical"):s.classList.remove("vertical")}))};this.setTabPanels=()=>{this.tabpanels.forEach(((e,t)=>{const i=this.tabIds[t];const s=this.tabpanelIds[t];e.setAttribute("id",s);e.setAttribute("aria-labelledby",i);this.activeTabIndex!==t?e.setAttribute("hidden",""):e.removeAttribute("hidden")}))};this.handleTabClick=e=>{const t=e.currentTarget;if(t.nodeType===1&&this.isFocusableElement(t)){this.prevActiveTabIndex=this.activeTabIndex;this.activeTabIndex=this.tabs.indexOf(t);this.setComponent()}};this.handleTabKeyDown=e=>{if(this.isHorizontal()){switch(e.key){case ii:e.preventDefault();this.adjustBackward(e);break;case si:e.preventDefault();this.adjustForward(e);break}}else{switch(e.key){case ni:e.preventDefault();this.adjustBackward(e);break;case ti:e.preventDefault();this.adjustForward(e);break}}switch(e.key){case ai:e.preventDefault();this.adjust(-this.activeTabIndex);break;case li:e.preventDefault();this.adjust(this.tabs.length-this.activeTabIndex-1);break}};this.adjustForward=e=>{const t=this.tabs;let i=0;i=this.activetab?t.indexOf(this.activetab)+1:1;if(i===t.length){i=0}while(i<t.length&&t.length>1){if(this.isFocusableElement(t[i])){this.moveToTabByIndex(t,i);break}else if(this.activetab&&i===t.indexOf(this.activetab)){break}else if(i+1>=t.length){i=0}else{i+=1}}};this.adjustBackward=e=>{const t=this.tabs;let i=0;i=this.activetab?t.indexOf(this.activetab)-1:0;i=i<0?t.length-1:i;while(i>=0&&t.length>1){if(this.isFocusableElement(t[i])){this.moveToTabByIndex(t,i);break}else if(i-1<0){i=t.length-1}else{i-=1}}};this.moveToTabByIndex=(e,t)=>{const i=e[t];this.activetab=i;this.prevActiveTabIndex=this.activeTabIndex;this.activeTabIndex=t;i.focus();this.setComponent()}}orientationChanged(){if(this.$fastController.isConnected){this.setTabs();this.setTabPanels();this.handleActiveIndicatorPosition()}}activeidChanged(e,t){if(this.$fastController.isConnected&&this.tabs.length<=this.tabpanels.length){this.prevActiveTabIndex=this.tabs.findIndex((t=>t.id===e));this.setTabs();this.setTabPanels();this.handleActiveIndicatorPosition()}}tabsChanged(){if(this.$fastController.isConnected&&this.tabs.length<=this.tabpanels.length){this.tabIds=this.getTabIds();this.tabpanelIds=this.getTabPanelIds();this.setTabs();this.setTabPanels();this.handleActiveIndicatorPosition()}}tabpanelsChanged(){if(this.$fastController.isConnected&&this.tabpanels.length<=this.tabs.length){this.tabIds=this.getTabIds();this.tabpanelIds=this.getTabPanelIds();this.setTabs();this.setTabPanels();this.handleActiveIndicatorPosition()}}getActiveIndex(){const e=this.activeid;if(e!==undefined){return this.tabIds.indexOf(this.activeid)===-1?0:this.tabIds.indexOf(this.activeid)}else{return 0}}getTabIds(){return this.tabs.map((e=>{var t;return(t=e.getAttribute("id"))!==null&&t!==void 0?t:`tab-${nr()}`}))}getTabPanelIds(){return this.tabpanels.map((e=>{var t;return(t=e.getAttribute("id"))!==null&&t!==void 0?t:`panel-${nr()}`}))}setComponent(){if(this.activeTabIndex!==this.prevActiveTabIndex){this.activeid=this.tabIds[this.activeTabIndex];this.focusTab();this.change()}}isHorizontal(){return this.orientation===Ad.horizontal}handleActiveIndicatorPosition(){if(this.showActiveIndicator&&this.activeindicator&&this.activeTabIndex!==this.prevActiveTabIndex){if(this.ticking){this.ticking=false}else{this.ticking=true;this.animateActiveIndicator()}}}animateActiveIndicator(){this.ticking=true;const e=this.isHorizontal()?"gridColumn":"gridRow";const t=this.isHorizontal()?"translateX":"translateY";const i=this.isHorizontal()?"offsetLeft":"offsetTop";const s=this.activeIndicatorRef[i];this.activeIndicatorRef.style[e]=`${this.activeTabIndex+1}`;const n=this.activeIndicatorRef[i];this.activeIndicatorRef.style[e]=`${this.prevActiveTabIndex+1}`;const o=n-s;this.activeIndicatorRef.style.transform=`${t}(${o}px)`;this.activeIndicatorRef.classList.add("activeIndicatorTransition");this.activeIndicatorRef.addEventListener("transitionend",(()=>{this.ticking=false;this.activeIndicatorRef.style[e]=`${this.activeTabIndex+1}`;this.activeIndicatorRef.style.transform=`${t}(0px)`;this.activeIndicatorRef.classList.remove("activeIndicatorTransition")}))}adjust(e){const t=this.tabs.filter((e=>this.isFocusableElement(e)));const i=t.indexOf(this.activetab);const s=gi(0,t.length-1,i+e);const n=this.tabs.indexOf(t[s]);if(n>-1){this.moveToTabByIndex(this.tabs,n)}}focusTab(){this.tabs[this.activeTabIndex].focus()}connectedCallback(){super.connectedCallback();this.tabIds=this.getTabIds();this.tabpanelIds=this.getTabPanelIds();this.activeTabIndex=this.getActiveIndex()}}f([s.attr],Fd.prototype,"orientation",void 0);f([s.attr],Fd.prototype,"activeid",void 0);f([s.observable],Fd.prototype,"tabs",void 0);f([s.observable],Fd.prototype,"tabpanels",void 0);f([(0,s.attr)({mode:"boolean"})],Fd.prototype,"activeindicator",void 0);f([s.observable],Fd.prototype,"activeIndicatorRef",void 0);f([s.observable],Fd.prototype,"showActiveIndicator",void 0);Me(Fd,n);const Ld={none:"none",both:"both",horizontal:"horizontal",vertical:"vertical"};const Pd=(e,t)=>s.html`
    <template
        class="
            ${e=>e.readOnly?"readonly":""}
            ${e=>e.resize!==Ld.none?`resize-${e.resize}`:""}"
    >
        <label
            part="label"
            for="control"
            class="${e=>e.defaultSlottedNodes&&e.defaultSlottedNodes.length?"label":"label label__hidden"}"
        >
            <slot ${(0,s.slotted)("defaultSlottedNodes")}></slot>
        </label>
        <textarea
            part="control"
            class="control"
            id="control"
            ?autofocus="${e=>e.autofocus}"
            cols="${e=>e.cols}"
            ?disabled="${e=>e.disabled}"
            form="${e=>e.form}"
            list="${e=>e.list}"
            maxlength="${e=>e.maxlength}"
            minlength="${e=>e.minlength}"
            name="${e=>e.name}"
            placeholder="${e=>e.placeholder}"
            ?readonly="${e=>e.readOnly}"
            ?required="${e=>e.required}"
            rows="${e=>e.rows}"
            ?spellcheck="${e=>e.spellcheck}"
            :value="${e=>e.value}"
            aria-atomic="${e=>e.ariaAtomic}"
            aria-busy="${e=>e.ariaBusy}"
            aria-controls="${e=>e.ariaControls}"
            aria-current="${e=>e.ariaCurrent}"
            aria-describedby="${e=>e.ariaDescribedby}"
            aria-details="${e=>e.ariaDetails}"
            aria-disabled="${e=>e.ariaDisabled}"
            aria-errormessage="${e=>e.ariaErrormessage}"
            aria-flowto="${e=>e.ariaFlowto}"
            aria-haspopup="${e=>e.ariaHaspopup}"
            aria-hidden="${e=>e.ariaHidden}"
            aria-invalid="${e=>e.ariaInvalid}"
            aria-keyshortcuts="${e=>e.ariaKeyshortcuts}"
            aria-label="${e=>e.ariaLabel}"
            aria-labelledby="${e=>e.ariaLabelledby}"
            aria-live="${e=>e.ariaLive}"
            aria-owns="${e=>e.ariaOwns}"
            aria-relevant="${e=>e.ariaRelevant}"
            aria-roledescription="${e=>e.ariaRoledescription}"
            @input="${(e,t)=>e.handleTextInput()}"
            @change="${e=>e.handleChange()}"
            ${(0,s.ref)("control")}
        ></textarea>
    </template>
`;class Md extends Fe{}class Hd extends(To(Md)){constructor(){super(...arguments);this.proxy=document.createElement("textarea")}}class zd extends Hd{constructor(){super(...arguments);this.resize=Ld.none;this.cols=20;this.handleTextInput=()=>{this.value=this.control.value}}readOnlyChanged(){if(this.proxy instanceof HTMLTextAreaElement){this.proxy.readOnly=this.readOnly}}autofocusChanged(){if(this.proxy instanceof HTMLTextAreaElement){this.proxy.autofocus=this.autofocus}}listChanged(){if(this.proxy instanceof HTMLTextAreaElement){this.proxy.setAttribute("list",this.list)}}maxlengthChanged(){if(this.proxy instanceof HTMLTextAreaElement){this.proxy.maxLength=this.maxlength}}minlengthChanged(){if(this.proxy instanceof HTMLTextAreaElement){this.proxy.minLength=this.minlength}}spellcheckChanged(){if(this.proxy instanceof HTMLTextAreaElement){this.proxy.spellcheck=this.spellcheck}}select(){this.control.select();this.$emit("select")}handleChange(){this.$emit("change")}validate(){super.validate(this.control)}}f([(0,s.attr)({mode:"boolean"})],zd.prototype,"readOnly",void 0);f([s.attr],zd.prototype,"resize",void 0);f([(0,s.attr)({mode:"boolean"})],zd.prototype,"autofocus",void 0);f([(0,s.attr)({attribute:"form"})],zd.prototype,"formId",void 0);f([s.attr],zd.prototype,"list",void 0);f([(0,s.attr)({converter:s.nullableNumberConverter})],zd.prototype,"maxlength",void 0);f([(0,s.attr)({converter:s.nullableNumberConverter})],zd.prototype,"minlength",void 0);f([s.attr],zd.prototype,"name",void 0);f([s.attr],zd.prototype,"placeholder",void 0);f([(0,s.attr)({converter:s.nullableNumberConverter,mode:"fromView"})],zd.prototype,"cols",void 0);f([(0,s.attr)({converter:s.nullableNumberConverter,mode:"fromView"})],zd.prototype,"rows",void 0);f([(0,s.attr)({mode:"boolean"})],zd.prototype,"spellcheck",void 0);f([s.observable],zd.prototype,"defaultSlottedNodes",void 0);Me(zd,Vl);const Vd=(e,t)=>s.html`
    <template
        class="
            ${e=>e.readOnly?"readonly":""}
        "
    >
        <label
            part="label"
            for="control"
            class="${e=>e.defaultSlottedNodes&&e.defaultSlottedNodes.length?"label":"label label__hidden"}"
        >
            <slot
                ${(0,s.slotted)({property:"defaultSlottedNodes",filter:td})}
            ></slot>
        </label>
        <div class="root" part="root">
            ${r(e,t)}
            <input
                class="control"
                part="control"
                id="control"
                @input="${e=>e.handleTextInput()}"
                @change="${e=>e.handleChange()}"
                ?autofocus="${e=>e.autofocus}"
                ?disabled="${e=>e.disabled}"
                list="${e=>e.list}"
                maxlength="${e=>e.maxlength}"
                minlength="${e=>e.minlength}"
                pattern="${e=>e.pattern}"
                placeholder="${e=>e.placeholder}"
                ?readonly="${e=>e.readOnly}"
                ?required="${e=>e.required}"
                size="${e=>e.size}"
                ?spellcheck="${e=>e.spellcheck}"
                :value="${e=>e.value}"
                type="${e=>e.type}"
                aria-atomic="${e=>e.ariaAtomic}"
                aria-busy="${e=>e.ariaBusy}"
                aria-controls="${e=>e.ariaControls}"
                aria-current="${e=>e.ariaCurrent}"
                aria-describedby="${e=>e.ariaDescribedby}"
                aria-details="${e=>e.ariaDetails}"
                aria-disabled="${e=>e.ariaDisabled}"
                aria-errormessage="${e=>e.ariaErrormessage}"
                aria-flowto="${e=>e.ariaFlowto}"
                aria-haspopup="${e=>e.ariaHaspopup}"
                aria-hidden="${e=>e.ariaHidden}"
                aria-invalid="${e=>e.ariaInvalid}"
                aria-keyshortcuts="${e=>e.ariaKeyshortcuts}"
                aria-label="${e=>e.ariaLabel}"
                aria-labelledby="${e=>e.ariaLabelledby}"
                aria-live="${e=>e.ariaLive}"
                aria-owns="${e=>e.ariaOwns}"
                aria-relevant="${e=>e.ariaRelevant}"
                aria-roledescription="${e=>e.ariaRoledescription}"
                ${(0,s.ref)("control")}
            />
            ${o(e,t)}
        </div>
    </template>
`;const Nd=(e,t)=>s.html`
    <template
        aria-label="${e=>e.ariaLabel}"
        aria-labelledby="${e=>e.ariaLabelledby}"
        aria-orientation="${e=>e.orientation}"
        orientation="${e=>e.orientation}"
        role="toolbar"
        @mousedown="${(e,t)=>e.mouseDownHandler(t.event)}"
        @focusin="${(e,t)=>e.focusinHandler(t.event)}"
        @keydown="${(e,t)=>e.keydownHandler(t.event)}"
        ${(0,s.children)({property:"childItems",attributeFilter:["disabled","hidden"],filter:(0,s.elements)(),subtree:true})}
    >
        <slot name="label"></slot>
        <div class="positioning-region" part="positioning-region">
            ${r(e,t)}
            <slot
                ${(0,s.slotted)({filter:(0,s.elements)(),property:"slottedItems"})}
            ></slot>
            ${o(e,t)}
        </div>
    </template>
`;const Bd=Object.freeze({[vi.ArrowUp]:{[il.i.vertical]:-1},[vi.ArrowDown]:{[il.i.vertical]:1},[vi.ArrowLeft]:{[il.i.horizontal]:{[Oi.N.ltr]:-1,[Oi.N.rtl]:1}},[vi.ArrowRight]:{[il.i.horizontal]:{[Oi.N.ltr]:1,[Oi.N.rtl]:-1}}});class Ud extends Fe{constructor(){super(...arguments);this._activeIndex=0;this.direction=Oi.N.ltr;this.orientation=il.i.horizontal}get activeIndex(){s.Observable.track(this,"activeIndex");return this._activeIndex}set activeIndex(e){if(this.$fastController.isConnected){this._activeIndex=gi(0,this.focusableElements.length-1,e);s.Observable.notify(this,"activeIndex")}}slottedItemsChanged(){if(this.$fastController.isConnected){this.reduceFocusableElements()}}mouseDownHandler(e){var t;const i=(t=this.focusableElements)===null||t===void 0?void 0:t.findIndex((t=>t.contains(e.target)));if(i>-1&&this.activeIndex!==i){this.setFocusedElement(i)}return true}childItemsChanged(e,t){if(this.$fastController.isConnected){this.reduceFocusableElements()}}connectedCallback(){super.connectedCallback();this.direction=no(this)}focusinHandler(e){const t=e.relatedTarget;if(!t||this.contains(t)){return}this.setFocusedElement()}getDirectionalIncrementer(e){var t,i,s,n,o;return(o=(s=(i=(t=Bd[e])===null||t===void 0?void 0:t[this.orientation])===null||i===void 0?void 0:i[this.direction])!==null&&s!==void 0?s:(n=Bd[e])===null||n===void 0?void 0:n[this.orientation])!==null&&o!==void 0?o:0}keydownHandler(e){const t=e.key;if(!(t in vi)||e.defaultPrevented||e.shiftKey){return true}const i=this.getDirectionalIncrementer(t);if(!i){return!e.target.closest("[role=radiogroup]")}const s=this.activeIndex+i;if(this.focusableElements[s]){e.preventDefault()}this.setFocusedElement(s);return true}get allSlottedItems(){return[...this.start.assignedElements(),...this.slottedItems,...this.end.assignedElements()]}reduceFocusableElements(){var e;const t=(e=this.focusableElements)===null||e===void 0?void 0:e[this.activeIndex];this.focusableElements=this.allSlottedItems.reduce(Ud.reduceFocusableItems,[]);const i=this.focusableElements.indexOf(t);this.activeIndex=Math.max(0,i);this.setFocusableElements()}setFocusedElement(e=this.activeIndex){var t;this.activeIndex=e;this.setFocusableElements();(t=this.focusableElements[this.activeIndex])===null||t===void 0?void 0:t.focus()}static reduceFocusableItems(e,t){var i,s,n,o;const r=t.getAttribute("role")==="radio";const a=(s=(i=t.$fastController)===null||i===void 0?void 0:i.definition.shadowOptions)===null||s===void 0?void 0:s.delegatesFocus;const l=Array.from((o=(n=t.shadowRoot)===null||n===void 0?void 0:n.querySelectorAll("*"))!==null&&o!==void 0?o:[]).some((e=>Wa(e)));if(!t.hasAttribute("disabled")&&!t.hasAttribute("hidden")&&(Wa(t)||r||a||l)){e.push(t);return e}if(t.childElementCount){return e.concat(Array.from(t.children).reduce(Ud.reduceFocusableItems,[]))}return e}setFocusableElements(){if(this.$fastController.isConnected&&this.focusableElements.length>0){this.focusableElements.forEach(((e,t)=>{e.tabIndex=this.activeIndex===t?0:-1}))}}}f([s.observable],Ud.prototype,"direction",void 0);f([s.attr],Ud.prototype,"orientation",void 0);f([s.observable],Ud.prototype,"slottedItems",void 0);f([s.observable],Ud.prototype,"slottedLabel",void 0);f([s.observable],Ud.prototype,"childItems",void 0);class qd{}f([(0,s.attr)({attribute:"aria-labelledby"})],qd.prototype,"ariaLabelledby",void 0);f([(0,s.attr)({attribute:"aria-label"})],qd.prototype,"ariaLabel",void 0);Me(qd,$i);Me(Ud,n,qd);const jd=(e,t)=>s.html`
        ${(0,s.when)((e=>e.tooltipVisible),s.html`
            <${e.tagFor(ro)}
                fixed-placement="true"
                auto-update-mode="${e=>e.autoUpdateMode}"
                vertical-positioning-mode="${e=>e.verticalPositioningMode}"
                vertical-default-position="${e=>e.verticalDefaultPosition}"
                vertical-inset="${e=>e.verticalInset}"
                vertical-scaling="${e=>e.verticalScaling}"
                horizontal-positioning-mode="${e=>e.horizontalPositioningMode}"
                horizontal-default-position="${e=>e.horizontalDefaultPosition}"
                horizontal-scaling="${e=>e.horizontalScaling}"
                horizontal-inset="${e=>e.horizontalInset}"
                vertical-viewport-lock="${e=>e.horizontalViewportLock}"
                horizontal-viewport-lock="${e=>e.verticalViewportLock}"
                dir="${e=>e.currentDirection}"
                ${(0,s.ref)("region")}
            >
                <div class="tooltip" part="tooltip" role="tooltip">
                    <slot></slot>
                </div>
            </${e.tagFor(ro)}>
        `)}
    `;const _d={top:"top",right:"right",bottom:"bottom",left:"left",start:"start",end:"end",topLeft:"top-left",topRight:"top-right",bottomLeft:"bottom-left",bottomRight:"bottom-right",topStart:"top-start",topEnd:"top-end",bottomStart:"bottom-start",bottomEnd:"bottom-end"};class Kd extends Fe{constructor(){super(...arguments);this.anchor="";this.delay=300;this.autoUpdateMode="anchor";this.anchorElement=null;this.viewportElement=null;this.verticalPositioningMode="dynamic";this.horizontalPositioningMode="dynamic";this.horizontalInset="false";this.verticalInset="false";this.horizontalScaling="content";this.verticalScaling="content";this.verticalDefaultPosition=undefined;this.horizontalDefaultPosition=undefined;this.tooltipVisible=false;this.currentDirection=Oi.N.ltr;this.showDelayTimer=null;this.hideDelayTimer=null;this.isAnchorHoveredFocused=false;this.isRegionHovered=false;this.handlePositionChange=e=>{this.classList.toggle("top",this.region.verticalPosition==="start");this.classList.toggle("bottom",this.region.verticalPosition==="end");this.classList.toggle("inset-top",this.region.verticalPosition==="insetStart");this.classList.toggle("inset-bottom",this.region.verticalPosition==="insetEnd");this.classList.toggle("center-vertical",this.region.verticalPosition==="center");this.classList.toggle("left",this.region.horizontalPosition==="start");this.classList.toggle("right",this.region.horizontalPosition==="end");this.classList.toggle("inset-left",this.region.horizontalPosition==="insetStart");this.classList.toggle("inset-right",this.region.horizontalPosition==="insetEnd");this.classList.toggle("center-horizontal",this.region.horizontalPosition==="center")};this.handleRegionMouseOver=e=>{this.isRegionHovered=true};this.handleRegionMouseOut=e=>{this.isRegionHovered=false;this.startHideDelayTimer()};this.handleAnchorMouseOver=e=>{if(this.tooltipVisible){this.isAnchorHoveredFocused=true;return}this.startShowDelayTimer()};this.handleAnchorMouseOut=e=>{this.isAnchorHoveredFocused=false;this.clearShowDelayTimer();this.startHideDelayTimer()};this.handleAnchorFocusIn=e=>{this.startShowDelayTimer()};this.handleAnchorFocusOut=e=>{this.isAnchorHoveredFocused=false;this.clearShowDelayTimer();this.startHideDelayTimer()};this.startHideDelayTimer=()=>{this.clearHideDelayTimer();if(!this.tooltipVisible){return}this.hideDelayTimer=window.setTimeout((()=>{this.updateTooltipVisibility()}),60)};this.clearHideDelayTimer=()=>{if(this.hideDelayTimer!==null){clearTimeout(this.hideDelayTimer);this.hideDelayTimer=null}};this.startShowDelayTimer=()=>{if(this.isAnchorHoveredFocused){return}if(this.delay>1){if(this.showDelayTimer===null)this.showDelayTimer=window.setTimeout((()=>{this.startHover()}),this.delay);return}this.startHover()};this.startHover=()=>{this.isAnchorHoveredFocused=true;this.updateTooltipVisibility()};this.clearShowDelayTimer=()=>{if(this.showDelayTimer!==null){clearTimeout(this.showDelayTimer);this.showDelayTimer=null}};this.getAnchor=()=>{const e=this.getRootNode();if(e instanceof ShadowRoot){return e.getElementById(this.anchor)}return document.getElementById(this.anchor)};this.handleDocumentKeydown=e=>{if(!e.defaultPrevented&&this.tooltipVisible){switch(e.key){case ri:this.isAnchorHoveredFocused=false;this.updateTooltipVisibility();this.$emit("dismiss");break}}};this.updateTooltipVisibility=()=>{if(this.visible===false){this.hideTooltip()}else if(this.visible===true){this.showTooltip();return}else{if(this.isAnchorHoveredFocused||this.isRegionHovered){this.showTooltip();return}this.hideTooltip()}};this.showTooltip=()=>{if(this.tooltipVisible){return}this.currentDirection=no(this);this.tooltipVisible=true;document.addEventListener("keydown",this.handleDocumentKeydown);s.DOM.queueUpdate(this.setRegionProps)};this.hideTooltip=()=>{if(!this.tooltipVisible){return}this.clearHideDelayTimer();if(this.region!==null&&this.region!==undefined){this.region.removeEventListener("positionchange",this.handlePositionChange);this.region.viewportElement=null;this.region.anchorElement=null;this.region.removeEventListener("mouseover",this.handleRegionMouseOver);this.region.removeEventListener("mouseout",this.handleRegionMouseOut)}document.removeEventListener("keydown",this.handleDocumentKeydown);this.tooltipVisible=false};this.setRegionProps=()=>{if(!this.tooltipVisible){return}this.region.viewportElement=this.viewportElement;this.region.anchorElement=this.anchorElement;this.region.addEventListener("positionchange",this.handlePositionChange);this.region.addEventListener("mouseover",this.handleRegionMouseOver,{passive:true});this.region.addEventListener("mouseout",this.handleRegionMouseOut,{passive:true})}}visibleChanged(){if(this.$fastController.isConnected){this.updateTooltipVisibility();this.updateLayout()}}anchorChanged(){if(this.$fastController.isConnected){this.anchorElement=this.getAnchor()}}positionChanged(){if(this.$fastController.isConnected){this.updateLayout()}}anchorElementChanged(e){if(this.$fastController.isConnected){if(e!==null&&e!==undefined){e.removeEventListener("mouseover",this.handleAnchorMouseOver);e.removeEventListener("mouseout",this.handleAnchorMouseOut);e.removeEventListener("focusin",this.handleAnchorFocusIn);e.removeEventListener("focusout",this.handleAnchorFocusOut)}if(this.anchorElement!==null&&this.anchorElement!==undefined){this.anchorElement.addEventListener("mouseover",this.handleAnchorMouseOver,{passive:true});this.anchorElement.addEventListener("mouseout",this.handleAnchorMouseOut,{passive:true});this.anchorElement.addEventListener("focusin",this.handleAnchorFocusIn,{passive:true});this.anchorElement.addEventListener("focusout",this.handleAnchorFocusOut,{passive:true});const e=this.anchorElement.id;if(this.anchorElement.parentElement!==null){this.anchorElement.parentElement.querySelectorAll(":hover").forEach((t=>{if(t.id===e){this.startShowDelayTimer()}}))}}if(this.region!==null&&this.region!==undefined&&this.tooltipVisible){this.region.anchorElement=this.anchorElement}this.updateLayout()}}viewportElementChanged(){if(this.region!==null&&this.region!==undefined){this.region.viewportElement=this.viewportElement}this.updateLayout()}connectedCallback(){super.connectedCallback();this.anchorElement=this.getAnchor();this.updateTooltipVisibility()}disconnectedCallback(){this.hideTooltip();this.clearShowDelayTimer();this.clearHideDelayTimer();super.disconnectedCallback()}updateLayout(){this.verticalPositioningMode="locktodefault";this.horizontalPositioningMode="locktodefault";switch(this.position){case _d.top:case _d.bottom:this.verticalDefaultPosition=this.position;this.horizontalDefaultPosition="center";break;case _d.right:case _d.left:case _d.start:case _d.end:this.verticalDefaultPosition="center";this.horizontalDefaultPosition=this.position;break;case _d.topLeft:this.verticalDefaultPosition="top";this.horizontalDefaultPosition="left";break;case _d.topRight:this.verticalDefaultPosition="top";this.horizontalDefaultPosition="right";break;case _d.bottomLeft:this.verticalDefaultPosition="bottom";this.horizontalDefaultPosition="left";break;case _d.bottomRight:this.verticalDefaultPosition="bottom";this.horizontalDefaultPosition="right";break;case _d.topStart:this.verticalDefaultPosition="top";this.horizontalDefaultPosition="start";break;case _d.topEnd:this.verticalDefaultPosition="top";this.horizontalDefaultPosition="end";break;case _d.bottomStart:this.verticalDefaultPosition="bottom";this.horizontalDefaultPosition="start";break;case _d.bottomEnd:this.verticalDefaultPosition="bottom";this.horizontalDefaultPosition="end";break;default:this.verticalPositioningMode="dynamic";this.horizontalPositioningMode="dynamic";this.verticalDefaultPosition=void 0;this.horizontalDefaultPosition="center";break}}}f([(0,s.attr)({mode:"boolean"})],Kd.prototype,"visible",void 0);f([s.attr],Kd.prototype,"anchor",void 0);f([s.attr],Kd.prototype,"delay",void 0);f([s.attr],Kd.prototype,"position",void 0);f([(0,s.attr)({attribute:"auto-update-mode"})],Kd.prototype,"autoUpdateMode",void 0);f([(0,s.attr)({attribute:"horizontal-viewport-lock"})],Kd.prototype,"horizontalViewportLock",void 0);f([(0,s.attr)({attribute:"vertical-viewport-lock"})],Kd.prototype,"verticalViewportLock",void 0);f([s.observable],Kd.prototype,"anchorElement",void 0);f([s.observable],Kd.prototype,"viewportElement",void 0);f([s.observable],Kd.prototype,"verticalPositioningMode",void 0);f([s.observable],Kd.prototype,"horizontalPositioningMode",void 0);f([s.observable],Kd.prototype,"horizontalInset",void 0);f([s.observable],Kd.prototype,"verticalInset",void 0);f([s.observable],Kd.prototype,"horizontalScaling",void 0);f([s.observable],Kd.prototype,"verticalScaling",void 0);f([s.observable],Kd.prototype,"verticalDefaultPosition",void 0);f([s.observable],Kd.prototype,"horizontalDefaultPosition",void 0);f([s.observable],Kd.prototype,"tooltipVisible",void 0);f([s.observable],Kd.prototype,"currentDirection",void 0);const Wd=(e,t)=>s.html`
    <template
        role="treeitem"
        slot="${e=>e.isNestedItem()?"item":void 0}"
        tabindex="-1"
        class="${e=>e.expanded?"expanded":""} ${e=>e.selected?"selected":""} ${e=>e.nested?"nested":""}
            ${e=>e.disabled?"disabled":""}"
        aria-expanded="${e=>e.childItems&&e.childItemLength()>0?e.expanded:void 0}"
        aria-selected="${e=>e.selected}"
        aria-disabled="${e=>e.disabled}"
        @focusin="${(e,t)=>e.handleFocus(t.event)}"
        @focusout="${(e,t)=>e.handleBlur(t.event)}"
        ${(0,s.children)({property:"childItems",filter:(0,s.elements)()})}
    >
        <div class="positioning-region" part="positioning-region">
            <div class="content-region" part="content-region">
                ${(0,s.when)((e=>e.childItems&&e.childItemLength()>0),s.html`
                        <div
                            aria-hidden="true"
                            class="expand-collapse-button"
                            part="expand-collapse-button"
                            @click="${(e,t)=>e.handleExpandCollapseButtonClick(t.event)}"
                            ${(0,s.ref)("expandCollapseButton")}
                        >
                            <slot name="expand-collapse-glyph">
                                ${t.expandCollapseGlyph||""}
                            </slot>
                        </div>
                    `)}
                ${r(e,t)}
                <slot></slot>
                ${o(e,t)}
            </div>
        </div>
        ${(0,s.when)((e=>e.childItems&&e.childItemLength()>0&&(e.expanded||e.renderCollapsedChildren)),s.html`
                <div role="group" class="items" part="items">
                    <slot name="item" ${(0,s.slotted)("items")}></slot>
                </div>
            `)}
    </template>
`;function Gd(e){return ur(e)&&e.getAttribute("role")==="treeitem"}class Yd extends Fe{constructor(){super(...arguments);this.expanded=false;this.focusable=false;this.isNestedItem=()=>Gd(this.parentElement);this.handleExpandCollapseButtonClick=e=>{if(!this.disabled&&!e.defaultPrevented){this.expanded=!this.expanded}};this.handleFocus=e=>{this.setAttribute("tabindex","0")};this.handleBlur=e=>{this.setAttribute("tabindex","-1")}}expandedChanged(){if(this.$fastController.isConnected){this.$emit("expanded-change",this)}}selectedChanged(){if(this.$fastController.isConnected){this.$emit("selected-change",this)}}itemsChanged(e,t){if(this.$fastController.isConnected){this.items.forEach((e=>{if(Gd(e)){e.nested=true}}))}}static focusItem(e){e.focusable=true;e.focus()}childItemLength(){const e=this.childItems.filter((e=>Gd(e)));return e?e.length:0}}f([(0,s.attr)({mode:"boolean"})],Yd.prototype,"expanded",void 0);f([(0,s.attr)({mode:"boolean"})],Yd.prototype,"selected",void 0);f([(0,s.attr)({mode:"boolean"})],Yd.prototype,"disabled",void 0);f([s.observable],Yd.prototype,"focusable",void 0);f([s.observable],Yd.prototype,"childItems",void 0);f([s.observable],Yd.prototype,"items",void 0);f([s.observable],Yd.prototype,"nested",void 0);f([s.observable],Yd.prototype,"renderCollapsedChildren",void 0);Me(Yd,n);const Xd=(e,t)=>s.html`
    <template
        role="tree"
        ${(0,s.ref)("treeView")}
        @keydown="${(e,t)=>e.handleKeyDown(t.event)}"
        @focusin="${(e,t)=>e.handleFocus(t.event)}"
        @focusout="${(e,t)=>e.handleBlur(t.event)}"
        @click="${(e,t)=>e.handleClick(t.event)}"
        @selected-change="${(e,t)=>e.handleSelectedChange(t.event)}"
    >
        <slot ${(0,s.slotted)("slottedTreeItems")}></slot>
    </template>
`;class Qd extends Fe{constructor(){super(...arguments);this.currentFocused=null;this.handleFocus=e=>{if(this.slottedTreeItems.length<1){return}if(e.target===this){if(this.currentFocused===null){this.currentFocused=this.getValidFocusableItem()}if(this.currentFocused!==null){Yd.focusItem(this.currentFocused)}return}if(this.contains(e.target)){this.setAttribute("tabindex","-1");this.currentFocused=e.target}};this.handleBlur=e=>{if(e.target instanceof HTMLElement&&(e.relatedTarget===null||!this.contains(e.relatedTarget))){this.setAttribute("tabindex","0")}};this.handleKeyDown=e=>{if(e.defaultPrevented){return}if(this.slottedTreeItems.length<1){return true}const t=this.getVisibleNodes();switch(e.key){case ai:if(t.length){Yd.focusItem(t[0])}return;case li:if(t.length){Yd.focusItem(t[t.length-1])}return;case ii:if(e.target&&this.isFocusableElement(e.target)){const t=e.target;if(t instanceof Yd&&t.childItemLength()>0&&t.expanded){t.expanded=false}else if(t instanceof Yd&&t.parentElement instanceof Yd){Yd.focusItem(t.parentElement)}}return false;case si:if(e.target&&this.isFocusableElement(e.target)){const t=e.target;if(t instanceof Yd&&t.childItemLength()>0&&!t.expanded){t.expanded=true}else if(t instanceof Yd&&t.childItemLength()>0){this.focusNextNode(1,e.target)}}return;case ti:if(e.target&&this.isFocusableElement(e.target)){this.focusNextNode(1,e.target)}return;case ni:if(e.target&&this.isFocusableElement(e.target)){this.focusNextNode(-1,e.target)}return;case oi:this.handleClick(e);return}return true};this.handleSelectedChange=e=>{if(e.defaultPrevented){return}if(!(e.target instanceof Element)||!Gd(e.target)){return true}const t=e.target;if(t.selected){if(this.currentSelected&&this.currentSelected!==t){this.currentSelected.selected=false}this.currentSelected=t}else if(!t.selected&&this.currentSelected===t){this.currentSelected=null}return};this.setItems=()=>{const e=this.treeView.querySelector("[aria-selected='true']");this.currentSelected=e;if(this.currentFocused===null||!this.contains(this.currentFocused)){this.currentFocused=this.getValidFocusableItem()}this.nested=this.checkForNestedItems();const t=this.getVisibleNodes();t.forEach((e=>{if(Gd(e)){e.nested=this.nested}}))};this.isFocusableElement=e=>Gd(e);this.isSelectedElement=e=>e.selected}slottedTreeItemsChanged(){if(this.$fastController.isConnected){this.setItems()}}connectedCallback(){super.connectedCallback();this.setAttribute("tabindex","0");s.DOM.queueUpdate((()=>{this.setItems()}))}handleClick(e){if(e.defaultPrevented){return}if(!(e.target instanceof Element)||!Gd(e.target)){return true}const t=e.target;if(!t.disabled){t.selected=!t.selected}return}focusNextNode(e,t){const i=this.getVisibleNodes();if(!i){return}const s=i[i.indexOf(t)+e];if(ur(s)){Yd.focusItem(s)}}getValidFocusableItem(){const e=this.getVisibleNodes();let t=e.findIndex(this.isSelectedElement);if(t===-1){t=e.findIndex(this.isFocusableElement)}if(t!==-1){return e[t]}return null}checkForNestedItems(){return this.slottedTreeItems.some((e=>Gd(e)&&e.querySelector("[role='treeitem']")))}getVisibleNodes(){return pr(this,"[role='treeitem']")||[]}}f([(0,s.attr)({attribute:"render-collapsed-nodes"})],Qd.prototype,"renderCollapsedNodes",void 0);f([s.observable],Qd.prototype,"currentSelected",void 0);f([s.observable],Qd.prototype,"slottedTreeItems",void 0);class Zd{constructor(e){this.listenerCache=new WeakMap;this.query=e}bind(e){const{query:t}=this;const i=this.constructListener(e);i.bind(t)();t.addListener(i);this.listenerCache.set(e,i)}unbind(e){const t=this.listenerCache.get(e);if(t){this.query.removeListener(t);this.listenerCache.delete(e)}}}class Jd extends Zd{constructor(e,t){super(e);this.styles=t}static with(e){return t=>new Jd(e,t)}constructListener(e){let t=false;const i=this.styles;return function s(){const{matches:n}=this;if(n&&!t){e.$fastController.addStyles(i);t=n}else if(!n&&t){e.$fastController.removeStyles(i);t=n}}}unbind(e){super.unbind(e);e.$fastController.removeStyles(this.styles)}}const eh=Jd.with(window.matchMedia("(forced-colors)"));const th=Jd.with(window.matchMedia("(prefers-color-scheme: dark)"));const ih=Jd.with(window.matchMedia("(prefers-color-scheme: light)"));class sh{constructor(e,t,i){this.propertyName=e;this.value=t;this.styles=i}bind(e){s.Observable.getNotifier(e).subscribe(this,this.propertyName);this.handleChange(e,this.propertyName)}unbind(e){s.Observable.getNotifier(e).unsubscribe(this,this.propertyName);e.$fastController.removeStyles(this.styles)}handleChange(e,t){if(e[t]===this.value){e.$fastController.addStyles(this.styles)}else{e.$fastController.removeStyles(this.styles)}}}const nh="not-allowed";const oh=`:host([hidden]){display:none}`;function rh(e){return`${oh}:host{display:${e}}`}const ah=br()?"focus-visible":"focus"},62899:(e,t,i)=>{i.d(t,{i:()=>s});const s={horizontal:"horizontal",vertical:"vertical"}},42586:(e,t,i)=>{i.d(t,{N:()=>s});var s;(function(e){e["ltr"]="ltr";e["rtl"]="rtl"})(s||(s={}))}}]);