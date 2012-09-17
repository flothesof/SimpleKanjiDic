# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 09:02:45 2012

@author: FL232714
"""

import xml.etree.cElementTree as ET

def example_xml():
    # returns example xml
     return """<doc>
    <character>
    <literal>亜</literal>
    <codepoint>
    <cp_value cp_type="ucs">4e9c</cp_value>
    <cp_value cp_type="jis208">16-01</cp_value>
    </codepoint>
    <radical>
    <rad_value rad_type="classical">7</rad_value>
    <rad_value rad_type="nelson_c">1</rad_value>
    </radical>
    <misc>
    <grade>8</grade>
    <stroke_count>7</stroke_count>
    <variant var_type="jis208">48-19</variant>
    <freq>1509</freq>
    <jlpt>1</jlpt>
    </misc>
    <dic_number>
    <dic_ref dr_type="nelson_c">43</dic_ref>
    <dic_ref dr_type="nelson_n">81</dic_ref>
    <dic_ref dr_type="halpern_njecd">3540</dic_ref>
    <dic_ref dr_type="halpern_kkld">2204</dic_ref>
    <dic_ref dr_type="heisig">1809</dic_ref>
    <dic_ref dr_type="gakken">1331</dic_ref>
    <dic_ref dr_type="oneill_names">525</dic_ref>
    <dic_ref dr_type="oneill_kk">1788</dic_ref>
    <dic_ref dr_type="moro" m_vol="1" m_page="0525">272</dic_ref>
    <dic_ref dr_type="henshall">997</dic_ref>
    <dic_ref dr_type="sh_kk">1616</dic_ref>
    <dic_ref dr_type="jf_cards">1032</dic_ref>
    <dic_ref dr_type="tutt_cards">1092</dic_ref>
    <dic_ref dr_type="kanji_in_context">1818</dic_ref>
    <dic_ref dr_type="kodansha_compact">35</dic_ref>
    <dic_ref dr_type="maniette">1827</dic_ref>
    </dic_number>
    <query_code>
    <q_code qc_type="skip">4-7-1</q_code>
    <q_code qc_type="sh_desc">0a7.14</q_code>
    <q_code qc_type="four_corner">1010.6</q_code>
    <q_code qc_type="deroo">3273</q_code>
    </query_code>
    <reading_meaning>
    <rmgroup>
    <reading r_type="pinyin">ya4</reading>
    <reading r_type="korean_r">a</reading>
    <reading r_type="korean_h">아</reading>
    <reading r_type="ja_on">ア</reading>
    <reading r_type="ja_kun">つ.ぐ</reading>
    <meaning>Asia</meaning>
    <meaning>rank next</meaning>
    <meaning>come after</meaning>
    <meaning>-ous</meaning>
    <meaning m_lang="fr">Asie</meaning>
    <meaning m_lang="fr">suivant</meaning>
    <meaning m_lang="fr">sub-</meaning>
    <meaning m_lang="fr">sous-</meaning>
    <meaning m_lang="es">pref. para indicar</meaning>
    <meaning m_lang="es">venir después de</meaning>
    <meaning m_lang="es">Asia</meaning>
    <meaning m_lang="pt">Ásia</meaning>
    <meaning m_lang="pt">próxima</meaning>
    <meaning m_lang="pt">o que vem depois</meaning>
    <meaning m_lang="pt">-ous</meaning>
    </rmgroup>
    <nanori>や</nanori>
    <nanori>つぎ</nanori>
    <nanori>つぐ</nanori>
    </reading_meaning>
    </character>
    <!-- Entry for Kanji: 唖 -->
    <character>
    <literal>唖</literal>
    <codepoint>
    <cp_value cp_type="ucs">5516</cp_value>
    <cp_value cp_type="jis208">16-2</cp_value>
    </codepoint>
    <radical>
    <rad_value rad_type="classical">30</rad_value>
    </radical>
    <misc>
    <stroke_count>10</stroke_count>
    <variant var_type="jis212">21-64</variant>
    <variant var_type="jis212">45-68</variant>
    </misc>
    <dic_number>
    <dic_ref dr_type="nelson_c">939</dic_ref>
    <dic_ref dr_type="nelson_n">795</dic_ref>
    <dic_ref dr_type="heisig">2958</dic_ref>
    <dic_ref dr_type="moro" m_vol="2" m_page="1066">3743</dic_ref>
    </dic_number>
    <query_code>
    <q_code qc_type="skip">1-3-7</q_code>
    <q_code qc_type="sh_desc">3d8.3</q_code>
    <q_code qc_type="four_corner">6101.7</q_code>
    </query_code>
    <reading_meaning>
    <rmgroup>
    <reading r_type="pinyin">ya1</reading>
    <reading r_type="korean_r">a</reading>
    <reading r_type="korean_h">아</reading>
    <reading r_type="ja_on">ア</reading>
    <reading r_type="ja_on">アク</reading>
    <reading r_type="ja_kun">おし</reading>
    <meaning>mute</meaning>
    <meaning>dumb</meaning>
    </rmgroup>
    </reading_meaning>
    </character>
    </doc>"""

def data_structure(xml):
    data_structure = {}
    tree = ET.fromstring(xml)
    for element in tree.findall('character'):
        literal = element.find('literal').text
        reading_meaning = element.find('reading_meaning')
        rmgroup = reading_meaning.find('rmgroup')        
        readings = rmgroup.findall('reading')
        ja_kun = []
        ja_on = []
        for item in readings:
            if item.attrib['r_type'] == 'ja_kun':
                ja_kun.append(item.text)
            elif item.attrib['r_type'] == 'ja_on':
                ja_on.append(item.text)
        meanings = rmgroup.findall('meaning')        
        meaning = []                
        for item in meanings:
            if item.attrib == {}:
                meaning.append(item.text)
        data_structure[literal] = [literal, ja_on, ja_kun, meaning]
    return data_structure

if __name__ == '__main__':
    
    
    xml = example_xml()
    
    tree=ET.fromstring(xml)
    
    for element in tree.findall('character'):
        print '-------------------'
        children = element.getchildren()
        for child in element.getchildren():
            print (child.tag, child.text) 
    
    data = data_structure(xml)
